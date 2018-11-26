from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.index, name = "index"),
    path("new/", views.new, name = "new"),
    path("edit/<int:task_id>", views.edit, name = "edit"),
    path("delete/<int:task_id>", views.delete, name = "delete"),
    path("complete/<int:task_id>", views.complete, name = "complete"),
    path("reset/<int:task_id>", views.reset, name = "reset"),
]
