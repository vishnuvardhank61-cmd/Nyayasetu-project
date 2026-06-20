from django.contrib import admin
from .models import Complaint

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ("tracking_id", "title", "user", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("tracking_id", "title", "user__username")