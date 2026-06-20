from django.urls import path
from . import views

app_name = 'helplines'

urlpatterns = [
    path('', views.helplines_list, name='list'),
]
