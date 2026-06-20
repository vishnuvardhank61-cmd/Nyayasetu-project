from django.urls import path
from . import views

app_name = 'violations'

urlpatterns = [
    # New Situation Engine routes
    path('', views.situation_list, name='list'),
    path('situation/<int:id>/', views.situation_detail, name='situation_detail'),
    
    # Legacy routes
    path('consequences/', views.violation_consequences, name='consequences_list'),
    path('consequence/<int:id>/', views.consequence_detail, name='consequence_detail'),
    
    # Static guides
    path("how-to-complain/", views.how_to_complain, name="how_to_complain"),
    path("traffic-rules/", views.traffic_guide, name="traffic_guide"),
]
