from django.db import models


class RightCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Right Category'
        verbose_name_plural = 'Right Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class FundamentalRight(models.Model):
    article_number = models.CharField(
        max_length=20,
        db_index=True,
        help_text='Example: "14", "19(1)(a)"'
    )
    title = models.CharField(max_length=200, db_index=True)
    category = models.ForeignKey(
        RightCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='rights'
    )

    legal_explanation = models.TextField(
        help_text='Official legal explanation of the right'
    )
    simple_explanation = models.TextField(
        help_text='Simple, non-technical explanation for common people'
    )
    violation_example = models.TextField(
        help_text='Example of what happens when this right is violated'
    )

    what_to_do = models.TextField(
        help_text='What steps should a person take if their rights are violated?'
    )
    where_to_complain = models.TextField(
        help_text='Where to file a complaint or petition'
    )
    court_remedy = models.TextField(
        help_text='What remedies are available through courts'
    )
    case_references = models.TextField(
        blank=True,
        help_text='Important case references and judgments'
    )

    keywords = models.CharField(
        max_length=300,
        blank=True,
        help_text='Comma-separated keywords for search'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Fundamental Right'
        verbose_name_plural = 'Fundamental Rights'
        ordering = ['article_number']
        indexes = [
            models.Index(fields=['article_number']),
            models.Index(fields=['title']),
            models.Index(fields=['category']),
        ]

    def __str__(self):
        return f"Article {self.article_number} - {self.title}"

class WorkplaceLaw(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    short_name = models.CharField(max_length=100, help_text="Common name (e.g., PoSH, PF Act)")
    applies_to = models.TextField(help_text="Who does this act apply to? (e.g. Any office with >10 employees)")
    
    description = models.TextField(help_text="General description of the law")
    employee_rights = models.TextField(help_text="What rights the employee has under this law")
    employer_duties = models.TextField(help_text="Mandatory obligations for the employer")
    violation_consequences = models.TextField(help_text="What happens if the employer breaks this law?")
    
    where_to_complain = models.TextField(help_text="Where mapping or exact department to file complaint")
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Workplace Law'
        verbose_name_plural = 'Workplace Laws'
        ordering = ['title']

    def __str__(self):
        return f"{self.title} ({self.short_name})"