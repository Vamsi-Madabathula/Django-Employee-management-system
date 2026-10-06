from django.shortcuts import render
from .models import Tasks
# Create your views here.

def tasks_list(request):
    tasks = Tasks.objects.all()

    # render used to display the HTML page
    return render(request,'tasks/task_list.html',{
        'tasks' : tasks
    })