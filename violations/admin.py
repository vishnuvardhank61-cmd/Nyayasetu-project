from django.contrib import admin
from .models import ViolationConsequence


@admin.register(ViolationConsequence)
class ViolationConsequenceAdmin(admin.ModelAdmin):
    list_display = ('fundamental_right', 'created_at')
    search_fields = ('fundamental_right__title',)
    fieldsets = (
        ('Associated Right', {
            'fields': ('fundamental_right',)
        }),
        ('Consequences', {
            'fields': ('immediate_effects', 'long_term_effects')
        }),
        ('Remedies', {
            'fields': ('legal_remedies', 'compensation_options', 'prevention_measures')
        }),
        ('Examples', {
            'fields': ('case_examples',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
