from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.db.models import Q
import logging

from .models import Helpline

logger = logging.getLogger(__name__)


@require_http_methods(["GET"])
def helplines_list(request):
    """List emergency helplines"""
    try:
        category = request.GET.get("category", "").strip()
        query = request.GET.get("q", "").strip()
        
        helplines = Helpline.objects.all()
        
        if category:
            helplines = helplines.filter(category=category)
        
        if query:
            helplines = helplines.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )
        
        return render(request, "helplines/list.html", {
            "helplines": helplines,
            "categories": Helpline.CATEGORY_CHOICES,
            "selected_category": category,
            "query": query,
        })
    
    except Exception as e:
        logger.error(f'Error loading helplines: {str(e)}')
        return render(request, "helplines/list.html", {"helplines": []})
