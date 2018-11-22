from django.db import models
from django.core import validators
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
    comment = models.TextField(max_length = 1024, blank = True, null = True)
    createDatetime = models.DateTimeField(auto_now_add=True)
    updateDatetime = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.taskName
