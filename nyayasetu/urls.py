"""
URL configuration for nyayasetu project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    # Core
    path('', include('core.urls')),
    # Authentication & Accounts
    path('accounts/', include('accounts.urls')),
    # Rights & Laws
    path('rights/', include('rights.urls')),
    path('women-safety/', include('women_safety.urls')),
    path('regional-laws/', include('regions.urls')),
    # Complaints & Violations
    path('complaints/', include('complaints.urls')),
    path('violations/', include('violations.urls')),
    # Government Services
    path('documents/', include('documents.urls')),
    path('services/', include('applications.urls')),
    # Emergency Resources
    path('police-stations/', include('police_stations.urls')),
    path('helplines/', include('helplines.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
