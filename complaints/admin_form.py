from django import forms
from .models import Complaint
from rights.models import FundamentalRight

class ComplaintReviewForm(forms.ModelForm):
    violated_right = forms.ModelChoiceField(
        queryset=FundamentalRight.objects.all().order_by("article_number"),
        required=False
    )

    class Meta:
        model = Complaint
        fields = ["status", "violated_right", "admin_remark"]
        widgets = {
            "status": forms.Select(attrs={"style": "width:100%; padding:10px;"}),
            "violated_right": forms.Select(attrs={"style": "width:100%; padding:10px;"}),
            "admin_remark": forms.Textarea(attrs={"rows": 4, "style": "width:100%; padding:10px;"}),
        }