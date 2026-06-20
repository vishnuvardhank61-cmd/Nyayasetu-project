from django.urls import path
from . import views

app_name = 'regions'

urlpatterns = [
    path('', views.region_list, name='list'),
    path('<int:state_id>/', views.region_laws, name='state_laws'),
    path('law/<int:id>/', views.law_detail, name='law_detail'),
]
