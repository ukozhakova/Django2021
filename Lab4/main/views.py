from django.shortcuts import render

from main.models import Task


def todo_list(request):
    todos = Task.objects.all()
    return render(request, 'todo_list.html', context={'todos': todos})


def completed_todo_list(request, pk):
    todo = Task.objects.filter(id=pk)
    return render(request, 'completed_todo_list.html', context={'todos': todo})