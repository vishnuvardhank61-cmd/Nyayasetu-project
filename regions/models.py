from django.db import models


class State(models.Model):
    """Indian states/union territories"""
    name = models.CharField(max_length=100, unique=True, db_index=True)
    code = models.CharField(max_length=5, unique=True)  # e.g., "JK", "DL"
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'State/UT'
        verbose_name_plural = 'States/UTs'
        ordering = ['name']
    
    def __str__(self):
        return self.name


class RegionalLaw(models.Model):
    """State-specific laws and rules"""
    
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='laws')
    
    title = models.CharField(max_length=200, db_index=True)
    act_name = models.CharField(
        max_length=200,
        help_text="Name of the Act or Law (e.g., Kashmir Administrative Act)"
    )
    
    description = models.TextField()
    key_provisions = models.TextField(
        help_text="Important provisions and details of the law"
    )
    
    who_it_applies_to = models.TextField(
        help_text="Who does this law apply to?"
    )
    
    penalties_punishments = models.TextField(
        blank=True,
        help_text="What are the penalties for violation?"
    )
    
    how_to_comply = models.TextField(
        help_text="How to comply with this law"
    )
    
    official_link = models.URLField(
        blank=True,
        help_text="Link to official government website for this law"
    )
    
    effective_date = models.DateField(
        blank=True,
        null=True,
        help_text="When did this law come into effect?"
    )
    
    keywords = models.CharField(max_length=300, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Regional Law'
        verbose_name_plural = 'Regional Laws'
        ordering = ['state', 'title']
        indexes = [
            models.Index(fields=['state']),
            models.Index(fields=['title']),
        ]
    
    def __str__(self):
        return f"{self.title} ({self.state.name})"
