import base64
from datetime import date
from io import BytesIO

from django.contrib.auth.models import User
from django.db import models
from django.core import validators
from PIL import Image, ImageDraw, ImageFont


# Create your models here.
class Task(models.Model):
    taskName = models.CharField(max_length = 150, blank = False)
    taskImportance = models.IntegerField(default = 3,
                                         blank = False,
                                         validators = [
                                            validators.MinValueValidator(1),
                                            validators.MaxValueValidator(5)
                                            ])
    dueDate = models.DateField(blank = True, null = True)
    doneDate = models.DateField(blank = True, null = True)
    comment = models.CharField(max_length = 1024, blank = True, null = True)
    createDatetime = models.DateTimeField(auto_now_add=True)
    updateDatetime = models.DateTimeField(auto_now = True)
    completedDatetime = models.DateTimeField(blank = True, null = True)
    taskOwnerId = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "tasks")

    def __str__(self):
        return self.taskName

    @classmethod
    def getTodaysCompletedTasks(cls):
        completedTasks = cls.objects.filter(\
            completedDatetime__date = date.today(),
            )
        return completedTasks

    @classmethod
    def getTaskGraph(cls, tasks):
        width = 1200
        height = 400
        graph = Image.new("RGB", (width, height), (100,0,0))
        draw = ImageDraw.Draw(graph)
        font_size = 24 #文字の大きさの指定
        font = ImageFont.truetype('tasks/static/ume-hgo4.ttf', font_size)

        # tasks = Task.objects.filter(completedDatetime__isnull=True).order_by("dueDate").order_by("-taskImportance")
        tasks = tasks.order_by("dueDate").order_by("-taskImportance")
        for i, task in enumerate(tasks):
            if task.dueDate is None:
                continue
            yoko = width - (task.dueDate - date.today()).days * font_size * 8 - 200
            if yoko >= width - len(task.taskName) * font_size:
                yoko = width - len(task.taskName) * font_size
            if yoko < 10:
                yoko = 10

            draw.text((yoko-5 , i * 30 + 15), task.taskName, (255,255,255), font)

            if i >= 10:
                break

        buffer = BytesIO()
        graph.save(buffer, format="PNG")
        base64Img = base64.b64encode(buffer.getvalue()).decode().replace("'", "")
        return base64Img
