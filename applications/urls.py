from django.urls import path
from . import views

app_name = 'applications'

urlpatterns = [
    path('', views.service_list, name='service_list'),
    path('apply/<int:service_id>/', views.apply_service, name='apply'),
    path('success/<int:app_id>/', views.application_success, name='application_success'),
    path('my/', views.my_applications, name='my_applications'),
    path('<int:app_id>/', views.application_detail, name='detail'),
]
