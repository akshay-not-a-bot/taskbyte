from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TaskList(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=300)
    prio = models.CharField(max_length=4)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.task
