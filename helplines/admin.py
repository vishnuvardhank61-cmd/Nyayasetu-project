from django.contrib import admin
from .models import Helpline


@admin.register(Helpline)
class HelplineAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'phone', 'state', 'availability')
    list_filter = ('category', 'state', 'availability')
    search_fields = ('name', 'phone', 'description')
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'category', 'state')
        }),
        ('Contact', {
            'fields': ('phone', 'phone_alternative', 'email', 'website')
        }),
        ('Details', {
            'fields': ('description', 'scope', 'availability', 'languages')
        }),
    )
