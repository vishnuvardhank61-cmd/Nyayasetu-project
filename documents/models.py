from django.db import models


class GovernmentDocument(models.Model):
    """Government documents with guides and resources"""
    
    DOCUMENT_TYPE_CHOICES = [
        ('identity', 'Identity Documents'),
        ('travel', 'Travel Documents'),
        ('registry', 'Registry & Licensing'),
        ('certificate', 'Certificates'),
        ('permit', 'Permits & Licenses'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=200, db_index=True)
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPE_CHOICES)
    
    description = models.TextField()
    purpose = models.TextField(help_text="Why is this document needed?")
    
    eligibility = models.TextField(help_text="Who is eligible to apply?")
    required_documents = models.TextField(help_text="List of required documents/files")
    
    step_by_step_guide = models.TextField(help_text="Step-by-step application process")
    fees = models.CharField(max_length=200, blank=True, help_text="Application fees")
    processing_time = models.CharField(max_length=200, blank=True, help_text="Expected processing time")
    
    official_website = models.URLField(help_text="Official government website link")
    alternative_guides = models.URLField(blank=True, help_text="Other helpful resources")
    
    guide_pdf = models.FileField(
        upload_to='documents/guides/',
        blank=True,
        help_text="PDF guide for this document"
    )
    
    common_mistakes = models.TextField(
        blank=True, 
        help_text="Common reasons for application rejection"
    )
    document_checklist = models.TextField(
        blank=True,
        help_text="Line-separated list of items needed (e.g., '2 Passport Photos', 'Aadhaar Card copy')"
    )
    direct_apply_available = models.BooleanField(
        default=False, 
        help_text="Can a citizen apply for this directly online?"
    )
    offline_centers = models.TextField(
        blank=True, 
        help_text="Where to go for offline application (e.g. MeeSeva, CSC, District Office)"
    )
    
    keywords = models.CharField(max_length=300, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Government Document'
        verbose_name_plural = 'Government Documents'
        ordering = ['document_type', 'name']
        indexes = [
            models.Index(fields=['document_type']),
            models.Index(fields=['name']),
        ]
    
    def __str__(self):
        return f"{self.name} ({self.get_document_type_display()})"
