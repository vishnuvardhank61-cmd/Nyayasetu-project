from django.urls import path
from . import views

app_name = 'women_safety'

urlpatterns = [
    path('', views.women_safety_list, name='list'),
    path('<int:id>/', views.women_safety_detail, name='detail'),
]
