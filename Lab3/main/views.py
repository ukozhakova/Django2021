from django.shortcuts import render

def todo_list(request):
    tasks = [
    {
        'task': 'Task 1',
        'created': '10/09/2018',
        'due_on': '12/09/2018',
        'owner': 'admin',
    },
    {
        'task': 'Task 2',
        'created': '10/09/2018',
        'due_on': '12/09/2018',
        'owner': 'admin',
    },
    {
        'task': 'Task 3',
        'created': '10/09/2018',
        'due_on': '12/09/2018',
        'owner': 'admin',
    },
    {
        'task': 'Task 4',
        'created': '10/09/2018',
        'due_on': '12/09/2018',
        'owner': 'admin',
    },
]
    context = {
        'tasks': tasks
    }
    return render(request, 'todo_list.html', context=context)


def completed_todo_list(request):
    tasks = [
    {
        'task': 'Task 0',
        'created': '10/09/2018',
        'due_on': '12/09/2018',
        'owner': 'admin',
    },
    ]
    context = {
        'tasks': tasks
    }
    return render(request, 'completed_todo_list.html', context=context)