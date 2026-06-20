from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages
import json, logging
from datetime import datetime

from .models import ApplicationService, UserApplication

logger = logging.getLogger(__name__)


@login_required
@require_http_methods(["GET"])
def service_list(request):
    """List available application services"""
    try:
        services = ApplicationService.objects.all()
        return render(request, "applications/service_list.html", {"services": services})
    except Exception as e:
        logger.error(f'Error loading services: {str(e)}')
        messages.error(request, 'An error occurred.')
        return render(request, "applications/service_list.html", {"services": []})


@login_required
@require_http_methods(["GET", "POST"])
def apply_service(request, service_id):
    """Apply for a government service"""
    service = get_object_or_404(ApplicationService, id=service_id)
    
# If the service is NOT direct_apply, users should just see the guide
    if not service.direct_apply and request.method == "POST":
        return redirect('applications:service_list')

    if request.method == "POST":
        try:
            form_data = {k: v for k, v in request.POST.items() if k != 'csrfmiddlewaretoken'}
            
            # Enhanced Tracking Number Logic
            ts = datetime.now().strftime('%M%S')
            app_number = f"NS-{datetime.now().year}-{service.name[:3].upper()}-{ts}"
            
            application = UserApplication.objects.create(
                user=request.user,
                service=service,
                application_number=app_number,
                form_data=form_data
            )
            
            logger.info(f'Application {app_number} submitted by {request.user.username}')
            return redirect('applications:application_success', app_id=application.id)
        
        except Exception as e:
            logger.error(f'Error submitting application: {str(e)}')
            messages.error(request, 'Error submitting application.')
    
    # Parse required fields for template
    fields = []
    if service.required_fields:
        try:
            fields_data = json.loads(service.required_fields)
            fields = fields_data.get('fields', [])
        except:
            fields = [f.strip() for f in service.required_fields.split(',')]

    # Partition logic: Display form only if direct_apply is True
    if not service.direct_apply:
        return render(request, "applications/service_guide.html", {
            "service": service,
            "fields": fields
        })

    return render(request, "applications/apply_service.html", {
        "service": service,
            "fields": fields
        })


@login_required
def application_success(request, app_id):
    """Celebratory success page with Tracking ID"""
    application = get_object_or_404(UserApplication, id=app_id, user=request.user)
    return render(request, "applications/success.html", {
        "application": application,
        "service": application.service
    })


@login_required
@require_http_methods(["GET"])
def my_applications(request):
    """View user's submitted applications"""
    try:
        applications = UserApplication.objects.filter(user=request.user).select_related('service')
        return render(request, "applications/my_applications.html", {"applications": applications})
    except Exception as e:
        logger.error(f'Error loading user applications: {str(e)}')
        return render(request, "applications/my_applications.html", {"applications": []})


@login_required
@require_http_methods(["GET"])
def application_detail(request, app_id):
    """View detailed application status"""
    try:
        application = get_object_or_404(UserApplication, id=app_id, user=request.user)
        return render(request, "applications/application_detail.html", {"application": application})
    except Exception as e:
        logger.error(f'Error loading application detail: {str(e)}')
        return render(request, "applications/application_detail.html", {"application": None})
