from django.shortcuts import render
from .models import Task
# Create your views here.

def index(request):
    tasks = Task.objects.all().order_by("-doneDate")
    return render(request, "tasks/index.html", {"tasks": tasks})
