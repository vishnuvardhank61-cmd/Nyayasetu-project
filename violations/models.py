from django.db import models
from rights.models import FundamentalRight


class ViolationConsequence(models.Model):
    """What happens when a right is violated"""
    
    fundamental_right = models.OneToOneField(
        FundamentalRight,
        on_delete=models.CASCADE,
        related_name='violation_consequence'
    )
    
    immediate_effects = models.TextField(
        help_text="What are the immediate effects of violation?"
    )
    
    long_term_effects = models.TextField(
        help_text="Long-term consequences"
    )
    
    legal_remedies = models.TextField(
        help_text="What legal remedies are available?"
    )
    
    compensation_options = models.TextField(
        blank=True,
        help_text="What compensation can be claimed?"
    )
    
    prevention_measures = models.TextField(
        help_text="How can such violations be prevented?"
    )
    
    case_examples = models.TextField(
        blank=True,
        help_text="Real case examples"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Violation Consequence'
        verbose_name_plural = 'Violation Consequences'
    
    def __str__(self):
        return f"Consequences of violating {self.fundamental_right.title}"


class ViolationSituation(models.Model):
    """Situation-based legal violations (e.g., Police bribe, Work harassment)"""
    
    CATEGORY_CHOICES = [
        ('traffic', 'Traffic Violations'),
        ('police', 'Police Issues'),
        ('workplace', 'Workplace Issues'),
        ('domestic', 'Domestic & Family'),
        ('discrimination', 'Discrimination'),
        ('medical', 'Medical & Healthcare'),
        ('consumer', 'Consumer Rights'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200, db_index=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    
    is_legal = models.BooleanField(
        default=False, 
        help_text="Is this action legal? (Checked = YES, Unchecked = NO)"
    )
    
    simple_explanation = models.TextField(
        help_text="Very simple English explanation of why this is/isn't legal"
    )
    
    step_by_step_guide = models.TextField(
        help_text="Numbered list: What should the user do now?"
    )
    
    where_to_complain = models.TextField(
        help_text="Exact authority, platform, or office to file a complaint"
    )
    
    legal_remedies = models.TextField(
        help_text="What legal actions can be taken?"
    )
    
    compensation_details = models.TextField(
        blank=True, 
        help_text="Is there any money or relief the user can claim?"
    )
    
    prevention_tips = models.TextField(
        blank=True, 
        help_text="How to avoid this situation in the future"
    )
    
    real_life_example = models.TextField(
        help_text="A story-based example of this situation"
    )
    
    landmark_judgment = models.TextField(
        blank=True,
        help_text="Supreme Court or High Court landmark judgments related to this situation"
    )
    
    related_right = models.ForeignKey(
        FundamentalRight, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='situations',
        help_text="Which Fundamental Right covers this situation?"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Violation Situation'
        verbose_name_plural = 'Violation Situations'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
