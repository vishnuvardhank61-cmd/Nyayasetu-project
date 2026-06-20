from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
import logging

from .models import GovernmentDocument

logger = logging.getLogger(__name__)


@require_http_methods(["GET"])
def document_list(request):
    """List all government documents"""
    try:
        doc_type = request.GET.get("type", "").strip()
        query = request.GET.get("q", "").strip()
        
        docs = GovernmentDocument.objects.all()
        
        if doc_type:
            docs = docs.filter(document_type=doc_type)
        
        if query:
            docs = docs.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(keywords__icontains=query)
            )
        
        paginator = Paginator(docs, 10)
        page_number = request.GET.get("page")
        
        try:
            page_obj = paginator.page(page_number)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
        
        return render(request, "documents/document_list.html", {
            "documents": page_obj,
            "page_obj": page_obj,
            "types": GovernmentDocument.DOCUMENT_TYPE_CHOICES,
            "query": query,
            "selected_type": doc_type,
            "total": paginator.count,
        })
    
    except Exception as e:
        logger.error(f'Error in document_list: {str(e)}')
        return render(request, "documents/document_list.html", {"documents": []})


@require_http_methods(["GET"])
def document_detail(request, id):
    """Show detailed guide for a document"""
    try:
        document = get_object_or_404(GovernmentDocument, id=id)
        related = GovernmentDocument.objects.filter(
            document_type=document.document_type
        ).exclude(id=document.id)[:5]
        
        # Try to find the corresponding ApplicationService for direct apply link
        from applications.models import ApplicationService
        service_slug = document.name.lower().replace(' ', '_').replace('/', '_')
        app_service = ApplicationService.objects.filter(name=service_slug).first()
        
        return render(request, "documents/document_detail.html", {
            "document": document,
            "related": related,
            "app_service": app_service,
        })
    
    except Exception as e:
        logger.error(f'Error loading document detail: {str(e)}')
        return render(request, "documents/document_detail.html", {"document": None})
