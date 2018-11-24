from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.index, name = "index"),
    path("new/", views.new, name = "new"),
    path("edit/<int:task_id>", views.edit, name = "edit"),
    path("edit2/<int:task_id>", views.edit2, name = "edit2")
]
