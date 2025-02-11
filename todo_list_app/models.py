from django.db import models

# Create your models here.

class TaskList(models.Model):
    task = models.CharField(max_length=300)
    prio = models.CharField(max_length=4)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.task