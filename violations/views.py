from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.db.models import Q
import logging

from .models import ViolationConsequence, ViolationSituation
from rights.models import FundamentalRight

logger = logging.getLogger(__name__)


@require_http_methods(["GET"])
def situation_list(request):
    """The Situation Engine: Main list with search and category filters"""
    try:
        query = request.GET.get('q', '')
        category = request.GET.get('category', '')
        
        situations = ViolationSituation.objects.all()
        
        if category:
            situations = situations.filter(category=category)
            
        if query:
            from django.db.models import Case, When, Value, IntegerField
            situations = situations.filter(
                Q(title__icontains=query) | 
                Q(simple_explanation__icontains=query) |
                Q(step_by_step_guide__icontains=query) |
                Q(where_to_complain__icontains=query) |
                Q(legal_remedies__icontains=query) |
                Q(real_life_example__icontains=query) |
                Q(prevention_tips__icontains=query)
            ).annotate(
                search_rank=Case(
                    When(title__icontains=query, then=Value(10)),
                    When(simple_explanation__icontains=query, then=Value(5)),
                    default=Value(1),
                    output_field=IntegerField(),
                )
            ).order_by('-search_rank', 'title')
            
        categories = ViolationSituation.CATEGORY_CHOICES
        
        return render(request, "violations/situation_list.html", {
            "situations": situations,
            "query": query,
            "selected_category": category,
            "categories": categories,
        })
    except Exception as e:
        logger.error(f'Error loading situation list: {str(e)}')
        return render(request, "violations/situation_list.html", {
            "situations": [],
            "categories": ViolationSituation.CATEGORY_CHOICES,
            "query": query or ""
        })


@require_http_methods(["GET"])
def situation_detail(request, id):
    """Detailed situation-to-action flow"""
    try:
        situation = get_object_or_404(ViolationSituation, id=id)
        return render(request, "violations/situation_detail.html", {
            "situation": situation,
            "right": situation.related_right,
        })
    except Exception as e:
        logger.error(f'Error loading situation detail: {str(e)}')
        return render(request, "violations/situation_detail.html", {"situation": None})


@require_http_methods(["GET"])
def violation_consequences(request):
    """Show consequences of rights violations (Legacy feature)"""
    try:
        # Optimized: Query consequences directly and join with rights
        consequences_data = ViolationConsequence.objects.select_related('fundamental_right').all()
        
        return render(request, "violations/consequences_list.html", {
            "consequences": consequences_data,
            "total": consequences_data.count(),
        })
    
    except Exception as e:
        logger.error(f'Error loading violation consequences: {str(e)}')
        messages.error(request, 'An error occurred while loading consequences.')
        return render(request, "violations/consequences_list.html", {"consequences": []})


@require_http_methods(["GET"])
def consequence_detail(request, id):
    """Detailed view of violation consequences (Legacy feature)"""
    try:
        consequence = get_object_or_404(ViolationConsequence, id=id)
        
        return render(request, "violations/consequence_detail.html", {
            "consequence": consequence,
            "right": consequence.fundamental_right,
        })
    
    except Exception as e:
        logger.error(f'Error loading consequence detail: {str(e)}')
        return render(request, "violations/consequence_detail.html", {"consequence": None})


@require_http_methods(["GET"])
def how_to_complain(request):
    """Step-by-step visual guide on where to file complaints"""
    return render(request, "violations/how_to_complain.html")


@require_http_methods(["GET"])
def traffic_guide(request):
    """Static but highly visual guide on handling Traffic Police and e-Challans"""
    return render(request, "violations/traffic_rules.html")
