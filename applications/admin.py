from django.contrib import admin
from .models import ApplicationService, UserApplication


@admin.register(ApplicationService)
class ApplicationServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'fees', 'processing_days')
    fieldsets = (
        ('Service Information', {
            'fields': ('name', 'description', 'eligibility')
        }),
        ('Details', {
            'fields': ('required_fields', 'fees', 'processing_days')
        }),
        ('Resources', {
            'fields': ('official_website', 'application_format_url')
        }),
    )


@admin.register(UserApplication)
class UserApplicationAdmin(admin.ModelAdmin):
    list_display = ('application_number', 'user', 'service', 'status', 'submitted_at')
    list_filter = ('status', 'service', 'submitted_at')
    search_fields = ('application_number', 'user__username')
    readonly_fields = ('submitted_at', 'updated_at')
    
    fieldsets = (
        ('Application', {
            'fields': ('application_number', 'user', 'service', 'status')
        }),
        ('Form Data', {
            'fields': ('form_data',)
        }),
        ('Review', {
            'fields': ('admin_notes', 'reviewed_by', 'completed_at')
        }),
        ('Timestamps', {
            'fields': ('submitted_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
