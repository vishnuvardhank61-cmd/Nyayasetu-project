from django.contrib import admin
from .models import WomenSafetyRight


@admin.register(WomenSafetyRight)
class WomenSafetyRightAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'legal_reference', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'legal_reference', 'keywords')
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'category')
        }),
        ('Legal Content', {
            'fields': ('legal_reference', 'description', 'rights_provided')
        }),
        ('Guidance', {
            'fields': ('how_to_get_help', 'prevention_tips', 'resources')
        }),
        ('Metadata', {
            'fields': ('keywords',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
