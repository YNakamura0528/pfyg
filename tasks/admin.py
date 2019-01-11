from django.contrib import admin
from .models import Task
# Register your models here.

class TasksAdmin(admin.ModelAdmin):
    list_display = ("id", "taskName", "dueDate", "createDatetime", "updateDatetime", "completedDatetime", "taskOwnerId" )
    list_display_links = ("id", "taskName", "taskOwnerId" )

admin.site.register(Task, TasksAdmin)

    # class Tasks(models.Model):
    #     taskName = models.CharField(max_length = 150, blank = False)
    #     taskImportance = models.IntegerField(default = 3,
    #                                          blank = False,
    #                                          validators = [
    #                                             validators.MinValueValidator(1),
    #                                             validators.MaxValueValidator(5)
    #                                             ])
    #     dueDate = models.DateField(blank = True, null = True)
    #     comment = models.TextField(max_length = 1024, blank = True, null = True)
    #     createdDatetime = models.DateTimeField(auto_now_add=True)
    #     updatedDatetime = models.DateTimeField(auto_now = True)
