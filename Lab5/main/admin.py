from django.contrib import admin
from main.models import TodoItem, TodoList

admin.site.register(TodoItem)
admin.site.register(TodoList)