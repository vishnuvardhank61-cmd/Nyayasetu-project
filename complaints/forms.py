from django import forms
from .models import Complaint
from rights.models import FundamentalRight


class ComplaintForm(forms.ModelForm):

    CATEGORY_CHOICES = [
        ("discrimination", "Discrimination"),
        ("police", "Police Misconduct"),
        ("freedom", "Freedom Violation"),
        ("exploitation", "Exploitation"),
        ("women_safety", "Women's Safety"),
        ("education", "Education Rights"),
        ("health", "Health Rights"),
        ("other", "Other"),
    ]

    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Complaint
        fields = ["title", "category", "description", "violated_right", "evidence"]
        widgets = {
            "evidence": forms.FileInput(attrs={
                "class": "form-control",
                "accept": ".pdf,.jpg,.jpeg,.png,.doc,.docx,.mp4,.mp3,.wav"
            }),
            "title": forms.TextInput(attrs={
                "placeholder": "Short title (e.g., Bribe demanded)",
                "class": "form-control",
                "maxlength": "200",
            }),
            "description": forms.Textarea(attrs={
                "placeholder": "Explain what happened in detail...",
                "rows": 6,
                "class": "form-control",
                "maxlength": "5000",
            }),
            "violated_right": forms.Select(attrs={
                "class": "form-control",
            }),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title and len(title) < 5:
            raise forms.ValidationError('Title must be at least 5 characters long.')
        return title
    
    def clean_description(self):
        description = self.cleaned_data.get('description')
        if description and len(description) < 20:
            raise forms.ValidationError('Description must be at least 20 characters long.')
        if description and len(description) > 5000:
            raise forms.ValidationError('Description cannot exceed 5000 characters.')
        return description