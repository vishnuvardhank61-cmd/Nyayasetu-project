from django.contrib import admin
from .models import State, RegionalLaw


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')


@admin.register(RegionalLaw)
class RegionalLawAdmin(admin.ModelAdmin):
    list_display = ('title', 'state', 'act_name', 'effective_date')
    list_filter = ('state', 'effective_date')
    search_fields = ('title', 'act_name', 'keywords')
    fieldsets = (
        ('Basic Information', {
            'fields': ('state', 'title', 'act_name')
        }),
        ('Content', {
            'fields': ('description', 'key_provisions', 'who_it_applies_to', 'penalties_punishments')
        }),
        ('Implementation', {
            'fields': ('how_to_comply', 'effective_date', 'official_link')
        }),
        ('Metadata', {
            'fields': ('keywords',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
