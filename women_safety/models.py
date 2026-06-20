from django.db import models


class WomenSafetyRight(models.Model):
    """Model for women-specific safety rights and laws"""
    
    CATEGORY_CHOICES = [
        ('personal', 'Personal Safety'),
        ('workplace', 'Workplace Rights'),
        ('property', 'Property Rights'),
        ('family', 'Family Law'),
        ('legal', 'Legal Protection'),
        ('health', 'Health & Medical Rights'),
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=200, db_index=True)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        db_index=True
    )
    
    description = models.TextField()
    rights_provided = models.TextField(help_text="What rights does a woman have?")
    penalties = models.TextField(blank=True, help_text="Penalties for violating this law")
    
    legal_reference = models.CharField(
        max_length=200,
        help_text="Law or Act reference (e.g., IPC 376, Dowry Prohibition Act)"
    )
    
    how_to_get_help = models.TextField(
        help_text="Step-by-step guide to access or exercise this right"
    )
    
    prevention_tips = models.TextField(
        blank=True,
        help_text="Prevention or protective tips"
    )
    
    resources = models.TextField(
        blank=True,
        help_text="Helpful organizations, helplines, websites"
    )
    
    keywords = models.CharField(
        max_length=300,
        blank=True,
        help_text="Comma-separated keywords for search"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Women's Safety Right"
        verbose_name_plural = "Women's Safety Rights"
        ordering = ['category', 'title']
        indexes = [
            models.Index(fields=['category']),
            models.Index(fields=['title']),
        ]
    
    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"
