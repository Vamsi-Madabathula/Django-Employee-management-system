#We need it because we are going to create a database model.
from django.db import models

# Create your models here.
# This means Employee inherits from Django's models.Model.
# So Django knows: "Employee is a Django database model."
# Because of this, Django can convert this class into a database table.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    joining_date = models.DateField()
    #This is a special Python method. 
    # It tells Django: When you display a Task object as text, what should you show?
    def __str__(self):
        return self.name





