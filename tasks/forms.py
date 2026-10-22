# Import Django's forms module.
from django import forms

# Import the Task model from our current app.
from .models import Tasks

# Create a form based on the Task model.
class TaskForm(forms.ModelForm):
     # Configure the form fields and model.
     class Meta:

            # Connect the form to our existing Tasks model.
            model = Tasks

            # Specify which fields users can fill in.
            fields = [ 
                        "title",
                        "description",
                        "assigned_to",
                        "priority",
                        "status",
                        "due_date",
                       
               ]
            # Display a date picker for the due date.
            widgets = {
                        'due_date':forms.DateInput(
                              attrs={'type':'date'}
                        ),
                  }