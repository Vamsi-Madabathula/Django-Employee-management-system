from django.db import models
from employees.models import Employee


# Create your models here.

class Tasks(models.Model):
    PRIORITY_CHOICES = [ 
        ('Low','Low'),
        ('Medium','Medium'),
        ('High','High'),
    ]

    STATUS_CHOICES = [
        ('Pending','Pending'),
        ('In Progress','In Progress'),
        ('Completed','Completed'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    assigined_to = models.ForeignKey(Employee, on_delete=models.CASCADE)
    priority = models.CharField(max_length=20 , choices=PRIORITY_CHOICES ,default='Medium')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    due_date = models.DateField()

    def __str__(self):
        return self.title