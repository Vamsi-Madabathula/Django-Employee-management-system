from django.shortcuts import render ,redirect
from .models import Employee
# Create your views here.

def employee_list(request):
    employees = Employee.objects.all()

    return render(request,'employees/employee_list.html', {
        'employees' : employees
    })

def add_employee(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        department = request.POST['department']
        joining_date = request.POST['joining_date']

        Employee.objects.create(
            name=name,
            email=email,
            phone=phone,
            department=department,
            joining_date=joining_date
        )

        return redirect('employee_list')
    # HERE BELOWLINE WE ARE NOT SENDING employee OBJECT TO TEMPLATE SO THE DATA WILL NOT DISPLAYED
    return render(request,'employees/employee_form.html')

def edit_employee(request,id):

    employee = Employee.objects.get(id=id)
    
    if request.method == 'POST':
        employee.name = request.POST['name']
        employee.email = request.POST['email']
        employee.phone = request.POST['phone']
        employee.department = request.POST['department']
        employee.joining_date = request.POST['joining_date']

        employee.save() 
        
        return redirect('employee_list')
    # HERE BELOWLINE WE ARE SENDING employee OBJECT TO TEMPLATE SO THE DATA WILL DISPLAYED
    return render(request, 'employees/employee_form.html',{
        'employee' : employee
    })

def delete_employee(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('employee_list')