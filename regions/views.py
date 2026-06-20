from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.db.models import Q
import logging

from .models import RegionalLaw, State

logger = logging.getLogger(__name__)


@require_http_methods(["GET"])
def region_list(request):
    """List all states/regions"""
    try:
        states = State.objects.all()
        laws = RegionalLaw.objects.select_related('state').all()
        return render(request, "regions/list.html", {
            "states": states,
            "laws": laws
        })
    except Exception as e:
        logger.error(f'Error in region_list: {str(e)}')
        return render(request, "regions/list.html", {"states": [], "laws": []})


@require_http_methods(["GET"])
def region_laws(request, state_id):
    """Laws for a specific state"""
    try:
        state = get_object_or_404(State, id=state_id)
        query = request.GET.get("q", "").strip()
        
        laws = RegionalLaw.objects.filter(state=state)
        
        if query:
            laws = laws.filter(
                Q(title__icontains=query) |
                Q(act_name__icontains=query) |
                Q(keywords__icontains=query)
            )
        
        paginator = Paginator(laws, 10)
        page_number = request.GET.get("page")
        
        try:
            page_obj = paginator.page(page_number)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
        
        return render(request, "regions/region_laws.html", {
            "state": state,
            "laws": page_obj,
            "page_obj": page_obj,
            "query": query,
            "total_results": paginator.count,
        })
    
    except Exception as e:
        logger.error(f'Error loading region laws: {str(e)}')
        messages.error(request, 'An error occurred.')
        return render(request, "regions/region_laws.html", {})


@require_http_methods(["GET"])
def law_detail(request, id):
    """Detailed view of a specific law"""
    try:
        law = get_object_or_404(RegionalLaw, id=id)
        similar_laws = RegionalLaw.objects.filter(
            state=law.state
        ).exclude(id=law.id)[:5]
        
        return render(request, "regions/law_detail.html", {
            "law": law,
            "similar_laws": similar_laws,
        })
    
    except Exception as e:
        logger.error(f'Error loading law detail: {str(e)}')
        return render(request, "regions/law_detail.html", {"law": None})
