from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Task
from .forms import TaskForm

from django.contrib.auth.models import User

# Create your views here.


def index(request, option = None):

    user_id = request.user.id
    user = User.objects.get(id=user_id)

    # tasks = Task.objects.filter(completedDatetime__isnull=True).order_by("dueDate")
    tasks = user.tasks.filter(completedDatetime__isnull=True).order_by("dueDate")
    if option:
        tasks = tasks.order_by(option)

    completedTasks = Task.getTodaysCompletedTasks()
    newform = TaskForm()
    forms = []
    for task in tasks:
        forms.append({"id": task.id, "form":TaskForm(instance = task)})

    taskGraphBase64 = Task.getTaskGraph(tasks)
    return render(request, "tasks/index.html", {"newform": newform, "forms": forms, "completedTasks": completedTasks, "taskGraphBase64": taskGraphBase64, "user": user})

@login_required
def new(request):
    form = TaskForm(request.POST)
    # form["taskOwnerId"] = request.user.id
    if form.is_valid():
        taskForm = form.save(commit = False)
        taskForm.taskOwnerId = request.user
        taskForm.save()

    return redirect("tasks:index")

@login_required
def edit(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            taskForm = form.save(commit = False)
            taskForm.taskOwnerId = request.user
            taskForm.save()
    return redirect("tasks:index")


@login_required
def delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST" and task.taskOwnerId == request.user:
        task.delete()
    return redirect("tasks:index")


@login_required
def complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST" and task.taskOwnerId == request.user:
        task.completedDatetime = timezone.datetime.now()
        task.save()

    return redirect("tasks:index")


@login_required
def reset(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.completedDatetime = None
        task.save()

    return redirect("tasks:index")
