from django.urls import path

from .views import todo_list, completed_todo_list

urlpatterns = [
    path('todos/', todo_list),
    path('todos/1/completed', completed_todo_list)
]