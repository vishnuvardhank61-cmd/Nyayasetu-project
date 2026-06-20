from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.db.models import Count, Q
from django.core.paginator import Paginator
from django.core.cache import cache
import logging

from .models import Complaint
from .forms import ComplaintForm
from .admin_form import ComplaintReviewForm
from rights.models import FundamentalRight

logger = logging.getLogger(__name__)

# Cache timeout in seconds
CACHE_TIMEOUT = 3600  # 1 hour


def detect_violated_right(category: str, description: str):
    """
    Improved keyword detection with better scoring and caching.
    Returns (best_right, confidence, matched_keywords)
    
    FIXED: No longer causes N+1 query problem - uses single cached query
    """
    text = f"{category or ''} {description or ''}".lower()
    
    # Get all rights from cache or database (single query)
    cache_key = 'fundamental_rights_all'
    rights = cache.get(cache_key)
    if rights is None:
        rights = list(FundamentalRight.objects.all())
        cache.set(cache_key, rights, CACHE_TIMEOUT)

    best = None
    best_score = 0
    best_matches = []

    for r in rights:
        keywords = (r.keywords or "").lower()
        kw_list = [k.strip() for k in keywords.split(",") if k.strip()]

        matches = []
        score = 0

        for k in kw_list:
            if k in text:
                matches.append(k)
                score += 2  # exact keyword match
            elif any(word.startswith(k) for word in text.split()):
                matches.append(k)
                score += 1  # partial match

        if score > best_score:
            best = r
            best_score = score
            best_matches = matches

    # confidence calculation
    if best_score >= 5:
        confidence = 90
    elif best_score >= 3:
        confidence = 75
    elif best_score >= 1:
        confidence = 60
    else:
        confidence = 0

    return best, confidence, best_matches


@login_required
@require_http_methods(["GET", "POST"])
def file_complaint(request):
    """File a new complaint with auto-detection of violated rights"""
    suggested_right = None
    confidence = None
    matches = []

    if request.method == "POST":
        form = ComplaintForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                category = form.cleaned_data.get("category")
                description = form.cleaned_data.get("description")

                detected, confidence, matches = detect_violated_right(category, description)
                suggested_right = detected

                # STEP 1: user clicked "Check Violated Right" (preview only)
                if "preview" in request.POST:
                    if detected and not form.cleaned_data.get("violated_right"):
                        form.initial["violated_right"] = detected.id

                    return render(request, "complaints/file_complaint.html", {
                        "form": form,
                        "suggested_right": suggested_right,
                        "confidence": confidence,
                        "matches": matches
                    })

                # STEP 2: user clicked "Confirm & Submit"
                if "submit" in request.POST:
                    complaint = form.save(commit=False)
                    complaint.user = request.user

                    chosen = form.cleaned_data.get("violated_right")
                    complaint.violated_right = chosen if chosen else detected

                    complaint.save()
                    
                    logger.info(f'Complaint filed by {request.user.username}: {complaint.tracking_id}')
                    messages.success(request, f'Complaint filed successfully! Tracking ID: {complaint.tracking_id}')
                    return redirect("complaints:my_complaints")
            
            except Exception as e:
                logger.error(f'Error filing complaint: {str(e)}')
                messages.error(request, 'An error occurred while filing your complaint.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ComplaintForm()

    return render(request, "complaints/file_complaint.html", {
        "form": form,
        "suggested_right": suggested_right,
        "confidence": confidence,
        "matches": matches
    })


@login_required
@require_http_methods(["GET"])
def my_complaints(request):
    """Display user's complaints with pagination"""
    try:
        complaints_list = Complaint.objects.filter(user=request.user).select_related('violated_right')
        
        paginator = Paginator(complaints_list, 10)
        page_number = request.GET.get('page')
        complaints = paginator.get_page(page_number)
        
        return render(request, "complaints/my_complaints.html", {"complaints": complaints})
    
    except Exception as e:
        logger.error(f'Error loading complaints for {request.user.username}: {str(e)}')
        messages.error(request, 'An error occurred while loading your complaints.')
        return render(request, "complaints/my_complaints.html", {"complaints": []})


@staff_member_required
@require_http_methods(["GET"])
def admin_complaints_list(request):
    """Admin view to manage all complaints"""
    try:
        status = request.GET.get("status", "").strip()
        q = request.GET.get("q", "").strip()

        complaints_list = Complaint.objects.all().select_related('user', 'violated_right').order_by("-created_at")

        if status and status in dict(Complaint.STATUS_CHOICES):
            complaints_list = complaints_list.filter(status=status)

        if q:
            complaints_list = complaints_list.filter(
                Q(tracking_id__icontains=q) | Q(title__icontains=q)
            )

        paginator = Paginator(complaints_list, 15)
        page_number = request.GET.get('page')
        complaints = paginator.get_page(page_number)

        return render(request, "complaints/admin_list.html", {
            "complaints": complaints,
            "status": status,
            "q": q,
            "status_choices": Complaint.STATUS_CHOICES,
        })
    
    except Exception as e:
        logger.error(f'Error in admin complaints list: {str(e)}')
        messages.error(request, 'An error occurred while loading complaints.')
        return render(request, "complaints/admin_list.html", {"complaints": []})


@staff_member_required
@require_http_methods(["GET", "POST"])
def admin_complaint_detail(request, id):
    """Admin view to review and respond to complaints"""
    try:
        complaint = get_object_or_404(Complaint, id=id)

        if request.method == "POST":
            form = ComplaintReviewForm(request.POST, instance=complaint)
            if form.is_valid():
                form.save()
                messages.success(request, 'Complaint updated successfully.')
                logger.info(f'Complaint {complaint.tracking_id} updated by {request.user.username}')
                return redirect("complaints:admin_list")
            else:
                messages.error(request, 'Please correct the errors below.')
        else:
            form = ComplaintReviewForm(instance=complaint)

        return render(request, "complaints/admin_detail.html", {
            "c": complaint,
            "form": form
        })
    
    except Exception as e:
        logger.error(f'Error loading complaint detail {id}: {str(e)}')
        messages.error(request, 'An error occurred while loading the complaint.')
        return redirect("complaints:admin_list")


@login_required
@require_http_methods(["GET"])
def dashboard(request):
    """User dashboard with complaint statistics"""
    try:
        complaints = Complaint.objects.filter(user=request.user)

        stats = complaints.aggregate(
            total=Count("id"),
            pending=Count("id", filter=Q(status="Pending")),
            review=Count("id", filter=Q(status="Under Review")),
            resolved=Count("id", filter=Q(status="Resolved")),
            rejected=Count("id", filter=Q(status="Rejected")),
        )

        return render(request, "complaints/dashboard.html", {
            "stats": stats
        })
    
    except Exception as e:
        logger.error(f'Error loading complaints dashboard: {str(e)}')
        messages.error(request, 'An error occurred while loading statistics.')
        return render(request, "complaints/dashboard.html", {"stats": {}})
