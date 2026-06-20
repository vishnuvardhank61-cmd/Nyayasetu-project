from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.db.models import Q
import math, logging

from .models import PoliceStation
from regions.models import State

logger = logging.getLogger(__name__)


def calculate_distance(lat1, lon1, lat2, lon2):
    """Calculate distance between two coordinates in km"""
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c


@require_http_methods(["GET"])
def stations_list(request):
    """List police stations with map"""
    try:
        state_id = request.GET.get("state", "").strip()
        city = request.GET.get("city", "").strip()
        
        stations = PoliceStation.objects.select_related('state').all()
        states = State.objects.all()
        
        if state_id:
            try:
                state_id = int(state_id)
                stations = stations.filter(state_id=state_id)
            except ValueError:
                pass
        
        if city:
            stations = stations.filter(city__icontains=city)
        
        return render(request, "police_stations/list.html", {
            "stations": stations[:50],  # Limit for map performance
            "states": states,
            "selected_state": state_id,
            "selected_city": city,
            "total": stations.count(),
        })
    
    except Exception as e:
        logger.error(f'Error loading stations: {str(e)}')
        return render(request, "police_stations/list.html", {"stations": []})


@require_http_methods(["GET"])
def station_detail(request, id):
    """Detailed station information"""
    try:
        station = get_object_or_404(PoliceStation, id=id)
        nearby = PoliceStation.objects.filter(
            city=station.city
        ).exclude(id=station.id)[:5]
        
        return render(request, "police_stations/detail.html", {
            "station": station,
            "nearby": nearby,
        })
    
    except Exception as e:
        logger.error(f'Error loading station detail: {str(e)}')
        return render(request, "police_stations/detail.html", {"station": None})
