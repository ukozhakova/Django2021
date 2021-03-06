from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User

Status = [
        ('Done','Done'),
        ('Not Done','Not Done')
    ]

class Task(models.Model):
    
    task = models.CharField(max_length=255)
    created = models.DateTimeField(default=datetime.now())
    due_on = models.DateTimeField(default=datetime.now() + timedelta(days=2))
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.CharField(max_length=8, choices=Status)

    class Meta:

        def __str__(self):
            return f"{self.task}"