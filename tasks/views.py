from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
# Create your views here.

def index(request):
    tasks = Task.objects.all().order_by("-dueDate")
    newform = TaskForm()
    forms = []
    for task in tasks:
        forms.append({"id": task.id, "form":TaskForm(instance = task)})


    print(TaskForm(instance = task))
    return render(request, "tasks/index.html", {"newform": newform, "forms": forms})

def new(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        form.save()

    return redirect("tasks:index")

def edit(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        task.taskImportance = request.POST["taskImportance"]
        print("VALIDATE    ",task.save())

    return redirect("tasks:index")

def edit2(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance = task)
        # print(request.POST["pk"])
        if form.is_valid():
            form.save()
    return redirect("tasks:index")
