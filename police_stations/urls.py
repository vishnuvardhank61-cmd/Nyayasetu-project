from django.urls import path
from . import views

app_name = 'police_stations'

urlpatterns = [
    path('', views.stations_list, name='list'),
    path('<int:id>/', views.station_detail, name='detail'),
]
