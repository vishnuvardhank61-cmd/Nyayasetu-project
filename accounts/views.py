from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_http_methods
import logging

from .forms import RegisterForm, LoginForm, ProfileForm

logger = logging.getLogger(__name__)


@require_http_methods(["GET", "POST"])
def register(request):
    """User registration view with dual-form support"""
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            try:
                user = register_form.save()
                messages.success(request, 'Registration successful! Please log in.')
                logger.info(f'New user registered: {user.username}')
                return redirect('accounts:login')
            except Exception as e:
                logger.error(f'Registration error: {str(e)}')
                messages.error(request, 'An error occurred during registration. Please try again.')
    else:
        register_form = RegisterForm()

    login_form = LoginForm()
    return render(request, 'auth.html', {
        'register_form': register_form, 
        'login_form': login_form, 
        'is_register': True
    })


@require_http_methods(["GET", "POST"])
def user_login(request):
    """User login view with dual-form support"""
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            try:
                login(request, login_form.user)
                messages.success(request, f'Welcome back, {login_form.user.username}!')
                logger.info(f'User logged in: {login_form.user.username}')
                next_page = request.GET.get('next', 'accounts:dashboard')
                return redirect(next_page)
            except Exception as e:
                logger.error(f'Login error: {str(e)}')
                messages.error(request, 'An error occurred during login.')
    else:
        login_form = LoginForm()

    register_form = RegisterForm()
    return render(request, 'auth.html', {
        'login_form': login_form, 
        'register_form': register_form, 
        'is_register': False
    })


@login_required
@require_http_methods(["GET"])
def user_logout(request):
    """User logout view"""
    username = request.user.username
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    logger.info(f'User logged out: {username}')
    return redirect('home')


@login_required
@require_http_methods(["GET"])
def dashboard(request):
    """User dashboard"""
    from complaints.models import Complaint
    
    # Calculate stats for user's complaints
    user_complaints = Complaint.objects.filter(user=request.user)
    stats = {
        'total': user_complaints.count(),
        'resolved': user_complaints.filter(status='Resolved').count(),
        'pending': user_complaints.filter(status='Pending').count(),
        'review': user_complaints.filter(status='Under Review').count(),
    }
    
    # Get recent complaints
    recent_complaints = user_complaints.order_by('-created_at')[:5]
    
    context = {
        'user': request.user,
        'user_type': request.user.get_user_type_display(),
        'stats': stats,
        'recent_complaints': recent_complaints,
    }
    return render(request, "accounts/dashboard.html", context)


@login_required
@require_http_methods(["GET", "POST"])
def profile(request):
    """User profile view and edit"""
    user = request.user

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Profile updated successfully!')
                logger.info(f'User profile updated: {user.username}')
                return redirect("accounts:profile")
            except Exception as e:
                logger.error(f'Profile update error for {user.username}: {str(e)}')
                messages.error(request, 'An error occurred while updating your profile.')
    else:
        form = ProfileForm(instance=user)

    from complaints.models import Complaint
    from applications.models import UserApplication

    context = {
        'form': form,
        'user_id': user.id,
        'date_joined': user.date_joined,
        'last_login': user.last_login,
        'complaint_count': Complaint.objects.filter(user=user).count(),
        'application_count': UserApplication.objects.filter(user=user).count(),
    }

    return render(request, "accounts/profile.html", context)


@login_required
@require_http_methods(["GET"])
def complaint_history(request):
    """Complaint history view"""
    return render(request, "accounts/complaint_history.html")


@login_required
@require_http_methods(["GET"])
def application_history(request):
    """Application history view"""
    return render(request, "accounts/application_history.html")