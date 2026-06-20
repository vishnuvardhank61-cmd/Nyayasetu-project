from django.contrib import admin
from .models import PoliceStation


@admin.register(PoliceStation)
class PoliceStationAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'district', 'city', 'phone')
    list_filter = ('state', 'district')
    search_fields = ('name', 'city', 'phone')
    fieldsets = (
        ('Location', {
            'fields': ('name', 'state', 'district', 'city', 'address')
        }),
        ('Contact', {
            'fields': ('phone', 'email', 'opening_hours')
        }),
        ('Maps', {
            'fields': ('latitude', 'longitude'),
            'description': 'Provide GPS coordinates'
        }),
        ('Additional', {
            'fields': ('jurisdiction', 'keywords'),
            'classes': ('collapse',)
        }),
    )
