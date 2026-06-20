from django.db import models
from django.conf import settings
from django.utils import timezone
import uuid
from rights.models import FundamentalRight


class Complaint(models.Model):

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Under Review", "Under Review"),
        ("Resolved", "Resolved"),
        ("Rejected", "Rejected"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='complaints'
    )

    tracking_id = models.CharField(
        max_length=20,
        unique=True,
        editable=False,
        db_index=True
    )

    title = models.CharField(
        max_length=200,
        db_index=True
    )

    description = models.TextField(
        max_length=5000
    )

    category = models.CharField(
        max_length=100,
        blank=True,
        db_index=True
    )

    violated_right = models.ForeignKey(
        FundamentalRight,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='complaints'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending",
        db_index=True
    )

    admin_remark = models.TextField(blank=True)
    
    evidence = models.FileField(
        upload_to='complaints/evidence/%Y/%m/%d/',
        blank=True,
        null=True,
        help_text="Upload supporting documents, photos, or recordings (Max 10MB)"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Complaint'
        verbose_name_plural = 'Complaints'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', '-created_at']),
            models.Index(fields=['status', '-created_at']),
            models.Index(fields=['tracking_id']),
        ]

    def save(self, *args, **kwargs):
        if not self.tracking_id:
            while True:
                tracking_id = uuid.uuid4().hex[:10].upper()
                if not Complaint.objects.filter(tracking_id=tracking_id).exists():
                    self.tracking_id = tracking_id
                    break
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.tracking_id} - {self.title}"