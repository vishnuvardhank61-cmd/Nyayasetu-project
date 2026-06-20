from django.urls import path
from . import views

app_name = 'rights'

urlpatterns = [
    path("", views.right_list, name="right_list"),
    path("<int:id>/", views.right_detail, name="right_detail"),
    path("workplace/", views.workplace_laws_list, name="workplace_laws_list"),
    path("workplace/<int:id>/", views.workplace_law_detail, name="workplace_law_detail"),
]