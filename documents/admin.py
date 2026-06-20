from django.contrib import admin
from .models import GovernmentDocument


@admin.register(GovernmentDocument)
class GovernmentDocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'document_type', 'created_at')
    list_filter = ('document_type', 'created_at')
    search_fields = ('name', 'keywords')
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'document_type')
        }),
        ('Description', {
            'fields': ('description', 'purpose', 'eligibility')
        }),
        ('Application Details', {
            'fields': ('required_documents', 'step_by_step_guide', 'fees', 'processing_time')
        }),
        ('Resources', {
            'fields': ('official_website', 'alternative_guides', 'guide_pdf')
        }),
        ('Metadata', {
            'fields': ('keywords',),
            'classes': ('collapse',)
        }),
    )
