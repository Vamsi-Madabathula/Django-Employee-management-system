from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Tasks
from .forms import TaskForm

# Create your views here.
# Display all tasks
@login_required # when the user login then the task_list will displayed
def tasks_list(request):
    tasks = Tasks.objects.all()

    # render used to display the HTML page
    return render(request,'tasks/task_list.html',{
        
        'tasks' : tasks
    })


# Create a new task
@login_required # when the user login then the task_create will displayed
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
    return render(request,'tasks/task_form.html',{
        'form': form
    })

#create task update 
@login_required # when the user login then the task_update will displayed
def task_update(request, id):
    #finds the task by its ID; returns a 404 page if it doesn't exit.
    task = get_object_or_404(Tasks,id=id)
    #checks wheather the user submitted the form.
    if request.method == 'POST':
        #loads submitted data into the existing task instead of creating a new one.
        form = TaskForm(request.POST, instance=task) #instance = task is important thing
        #checks that the submitted values are valid.
        if form.is_valid():
            # saves the updated task to SQLite
            form.save()
            # returns the user to the tasklist after saving
            return redirect('tasks_list')
    else:
        # Dispaly the current task values in the form.
        form = TaskForm(instance=task)
    return render(request,'tasks/task_form.html',{'form':form})


#created the tass_deleted views
@login_required # when the user login then the task_delete will displayed
def task_delete(request, id):
    # finds the task or return 404 respose
    task = get_object_or_404(Tasks,id=id)
    #checks whether the user confirme deletion
    if request.method == 'POST':
        #deletes the selected task from the database
        task.delete()
        # returns to the task list
        return redirect('tasks_list')#tasks_list
    # display the confirmation page before deletion
    return render(
        request,
        'tasks/task_confirm_delete.html',
        {'task':task }                                                                                                                                                                                                                                                                                                                                                                                   
    )
