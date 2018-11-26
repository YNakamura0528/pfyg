from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Task
from .forms import TaskForm

# Create your views here.

def index(request):
    tasks = Task.objects.filter(completedDatetime__isnull=True).order_by("dueDate")
    completedTasks = Task.getTodaysCompletedTasks()
    newform = TaskForm()
    forms = []
    for task in tasks:
        forms.append({"id": task.id, "form":TaskForm(instance = task)})

    return render(request, "tasks/index.html", {"newform": newform, "forms": forms, "completedTasks": completedTasks})

def new(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        form.save()

    return redirect("tasks:index")

def edit(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
    return redirect("tasks:index")

def delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.delete()
    return redirect("tasks:index")

def complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.completedDatetime = timezone.datetime.now()
        task.save()

    return redirect("tasks:index")

def reset(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.completedDatetime = None
        task.save()

    return redirect("tasks:index")
