from django.db import models
from regions.models import State


class Helpline(models.Model):
    """Emergency helplines and support services"""
    
    CATEGORY_CHOICES = [
        ('emergency', 'Emergency Services'),
        ('women_safety', 'Women Safety'),
        ('child_safety', 'Child Safety'),
        ('mental_health', 'Mental Health'),
        ('legal_aid', 'Legal Aid'),
        ('labor', 'Labor Rights'),
        ('environment', 'Environment'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=200, db_index=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, db_index=True)
    
    phone = models.CharField(max_length=15)
    phone_alternative = models.CharField(max_length=15, blank=True)
    
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    
    description = models.TextField()
    scope = models.CharField(max_length=100, help_text="National / State / City")
    
    state = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='helplines'
    )
    
    availability = models.CharField(
        max_length=200,
        default="24/7",
        help_text="Availability hours"
    )
    
    languages = models.CharField(
        max_length=200,
        blank=True,
        help_text="Languages supported (comma-separated)"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Helpline'
        verbose_name_plural = 'Helplines'
        ordering = ['category', 'scope']
        indexes = [
            models.Index(fields=['category']),
            models.Index(fields=['state']),
        ]
    
    def __str__(self):
        return f"{self.name} ({self.phone})"
