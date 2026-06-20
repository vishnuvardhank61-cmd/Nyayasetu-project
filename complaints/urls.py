from django.urls import path
from . import views

app_name = "complaints"

urlpatterns = [
    path("file/", views.file_complaint, name="file_complaint"),
    path("my/", views.my_complaints, name="my_complaints"),
    path("manage/", views.admin_complaints_list, name="admin_list"),
    path("manage/<int:id>/", views.admin_complaint_detail, name="admin_detail"),
    path("dashboard/", views.dashboard, name="dashboard"),
]