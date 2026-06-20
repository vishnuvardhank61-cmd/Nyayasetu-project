from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
import logging

from .models import FundamentalRight, RightCategory, WorkplaceLaw

logger = logging.getLogger(__name__)


@require_http_methods(["GET"])
def right_list(request):
    """Display list of fundamental rights with filtering and search"""
    try:
        query = request.GET.get("q", "").strip()
        category_id = request.GET.get("category", "").strip()

        # Optimized query with prefetch
        rights = FundamentalRight.objects.select_related('category').all()
        categories = RightCategory.objects.all()

        # Filter by category
        if category_id:
            try:
                category_id = int(category_id)
                rights = rights.filter(category_id=category_id)
            except (ValueError, TypeError):
                pass

        # Search by text
        if query:
            from django.db.models import Q
            rights = rights.filter(
                Q(article_number__icontains=query) |
                Q(title__icontains=query) |
                Q(keywords__icontains=query) |
                Q(simple_explanation__icontains=query)
            )

        return render(request, "rights/list.html", {
            "rights": rights,
            "categories": categories,
            "query": query,
            "selected_category": category_id,
            "total_results": rights.count(),
        })
    
    except Exception as e:
        logger.error(f'Error in right_list: {str(e)}')
        messages.error(request, 'An error occurred while loading rights.')
        return render(request, "rights/list.html", {
            "rights": [],
            "categories": RightCategory.objects.all(),
        })


@require_http_methods(["GET"])
def right_detail(request, id):
    """Display detailed information about a specific right"""
    try:
        right = get_object_or_404(
            FundamentalRight.objects.select_related('category'),
            id=id
        )
        
        # Get related rights from same category
        related_rights = (
            FundamentalRight.objects.filter(category=right.category)
            .exclude(id=right.id)
            .order_by('article_number')[:5]
        )
        
        return render(request, "rights/detail.html", {
            "right": right,
            "related_rights": related_rights,
        })
    
    except Exception as e:
        logger.error(f'Error loading right detail {id}: {str(e)}')
        messages.error(request, 'An error occurred while loading this right.')
        return render(request, "rights/detail.html", {"right": None})


@require_http_methods(["GET"])
def workplace_laws_list(request):
    """List out corporate and workplace laws"""
    try:
        query = request.GET.get("q", "").strip()
        laws = WorkplaceLaw.objects.all()
        
        if query:
            from django.db.models import Q
            laws = laws.filter(
                Q(title__icontains=query) |
                Q(short_name__icontains=query) |
                Q(applies_to__icontains=query)
            )

        paginator = Paginator(laws, 10)
        page_number = request.GET.get("page")
        
        try:
            page_obj = paginator.page(page_number)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
            
        return render(request, "rights/workplace_list.html", {
            "laws": page_obj,
            "page_obj": page_obj,
            "paginator": paginator,
            "total": paginator.count,
            "query": query
        })
    except Exception as e:
        logger.error(f'Error loading workplace laws list: {str(e)}')
        return render(request, "rights/workplace_list.html", {"laws": []})


@require_http_methods(["GET"])
def workplace_law_detail(request, id):
    """Detailed view for a workplace law"""
    try:
        law = get_object_or_404(WorkplaceLaw, id=id)
        other_laws = WorkplaceLaw.objects.exclude(id=id)[:5]
        return render(request, "rights/workplace_detail.html", {"law": law, "other_laws": other_laws})
    except Exception as e:
        logger.error(f'Error loading workplace law detail: {str(e)}')
        return render(request, "rights/workplace_detail.html", {"law": None})