from django.db import models
from django.conf import settings


class ApplicationService(models.Model):
    """Government services available for online application"""
    
    SERVICE_CHOICES = [
        ('aadhaar_card', 'Aadhaar Card'),
        ('pan_card', 'PAN Card'),
        ('passport', 'Passport'),
        ('driving_license', 'Driving License'),
        ('voter_id', 'Voter ID'),
        ('income_certificate', 'Income Certificate'),
        ('caste_certificate', 'Caste Certificate'),
        ('birth_death_certificate', 'Birth/Death Certificate'),
        ('ration_card', 'Ration Card'),
    ]
    
    name = models.CharField(max_length=200, choices=SERVICE_CHOICES, unique=True)
    description = models.TextField()
    eligibility = models.TextField()
    required_fields = models.TextField(help_text="JSON or comma-separated list of required fields")
    fees = models.CharField(max_length=200)
    processing_days = models.IntegerField(help_text="Average processing time in days")
    
    direct_apply = models.BooleanField(
        default=True, 
        help_text="If True, user can apply directly on this site. If False, we point to offline/govt centers."
    )
    offline_instructions = models.TextField(
        blank=True, 
        help_text="Instructions for MeeSeva / CSC / Office applications if direct_apply is False."
    )
    
    requires_physical_verification = models.BooleanField(
        default=False,
        help_text="Set to True if the applicant must physically visit a center for biometrics or document verification."
    )
    
    official_website = models.URLField(blank=True, help_text="Verified government portal URL")
    application_format_url = models.URLField(blank=True, help_text="Link to official PDF or application format")
    
    class Meta:
        verbose_name = 'Application Service'
        verbose_name_plural = 'Application Services'
    
    def __str__(self):
        return self.get_name_display()


class UserApplication(models.Model):
    """User's submitted application"""
    
    STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('under_review', 'Under Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applications')
    service = models.ForeignKey(ApplicationService, on_delete=models.CASCADE)
    
    application_number = models.CharField(max_length=50, unique=True, db_index=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='submitted', db_index=True)
    
    # Dynamic form data stored as JSON
    form_data = models.JSONField(help_text="Application form data")
    
    # Admin notes
    admin_notes = models.TextField(blank=True)
    reviewed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='reviewed_applications'
    )
    
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'User Application'
        verbose_name_plural = 'User Applications'
        ordering = ['-submitted_at']
        indexes = [
            models.Index(fields=['user', '-submitted_at']),
            models.Index(fields=['status']),
        ]
    
    def __str__(self):
        return f"{self.application_number} - {self.service.get_name_display()}"
