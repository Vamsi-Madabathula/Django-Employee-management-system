from django.shortcuts import render, redirect
from .models import Tasks
from .forms import TaskForm

# Create your views here.
# Display all tasks
def tasks_list(request):
    tasks = Tasks.objects.all()

    # render used to display the HTML page
    return render(request,'tasks/task_list.html',{
        'tasks' : tasks
    })


# Create a new task
def task_create(request):


    # Check whether the form was submitted
    if request.method == 'POST':

        # Receive and validate the submitted data
        form = TaskForm(request.POST)

        # Check whether the submitted data is valid
        if form.is_valid():

            # Save the new task in the database
            form.save()

            # Redirect to the task list page
            return redirect('tasks_list')
    else:
        # Display an empty form for a new task
        form = TaskForm()

    # Open the task form page
    return redirect(request,'tasks/task_form.html',{
        'form': form
    })