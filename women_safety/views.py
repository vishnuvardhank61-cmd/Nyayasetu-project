from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.db.models import Q
import logging

from .models import WomenSafetyRight

logger = logging.getLogger(__name__)


@require_http_methods(["GET"])
def women_safety_list(request):
    """Display list of women's safety rights with filtering"""
    try:
        query = request.GET.get("q", "").strip()
        category = request.GET.get("category", "").strip()
        
        rights = WomenSafetyRight.objects.all()
        
        # Filter by category
        if category:
            rights = rights.filter(category=category)
        
        # Search
        if query:
            rights = rights.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(keywords__icontains=query)
            )
        
        # Pagination
        paginator = Paginator(rights, 10)
        page_number = request.GET.get("page")
        
        try:
            page_obj = paginator.page(page_number)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
        
        return render(request, "women_safety/list.html", {
            "women_safety_rights": page_obj,
            "page_obj": page_obj,
            "query": query,
            "categories": WomenSafetyRight.CATEGORY_CHOICES,
            "selected_category": category,
            "total_results": paginator.count,
        })
    
    except Exception as e:
        logger.error(f'Error in women_safety_list: {str(e)}')
        messages.error(request, 'An error occurred.')
        return render(request, "women_safety/safety_list.html", {
            "rights": [],
            "categories": WomenSafetyRight.CATEGORY_CHOICES,
        })


@require_http_methods(["GET"])
def women_safety_detail(request, id):
    """Display detailed women's safety information"""
    try:
        right = get_object_or_404(WomenSafetyRight, id=id)
        related = WomenSafetyRight.objects.filter(
            category=right.category
        ).exclude(id=right.id)[:5]
        
        return render(request, "women_safety/detail.html", {
            "right": right,
            "related": related,
        })
    
    except Exception as e:
        logger.error(f'Error loading safety detail: {str(e)}')
        messages.error(request, 'An error occurred.')
        return render(request, "women_safety/detail.html", {"right": None})
