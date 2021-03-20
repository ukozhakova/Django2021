from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class TodoList(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        
    def __str__(self):
        return f"{self.name}"


class TodoItem(models.Model):
    TYPE = [
        ('D', 'Done'),
        ('ND', 'Not Done')
    ]
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    due_on = models.DateTimeField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mark = models.CharField(max_length=2, choices=TYPE)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name='todo_items')

    class Meta:
        
    def __str__(self):
        return f"{self.title}"
