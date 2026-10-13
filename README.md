# Employee and Task Management System

A web-based Employee and Task Management System built with **Python and Django**. The application helps manage employee records and tasks through a simple web interface.

## Project Overview

This project demonstrates how to build a CRUD-based web application using Django. Users can manage employee information and create tasks assigned to employees. The project uses Django templates for the frontend and SQLite as the initial database.

## Features

### Employee Management
- Add new employee records.
- View the employee list and employee details.
- Update employee information.
- Delete employee records.
- Store details such as name, email, phone, department, and joining date.

### Task Management
- Create tasks and assign them to employees.
- View the task list.
- Update task information.
- Track task priority: Low, Medium, or High.
- Track task status: Pending, In Progress, or Completed.
- Store a task description and due date.

> Features such as authentication, permissions, search and filtering, dashboard summaries, and REST APIs can be added as development continues. Only list these as completed once they are implemented in your project.

## Technology Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Django Templates
- **Database:** SQLite
- **Development tools:** Visual Studio Code, Git, GitHub

## Project Structure

```text
employee_task_management/
├── manage.py
├── employee_task_management/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── employees/
│   ├── migrations/
│   ├── templates/
│   │   └── employees/
│   ├── static/
│   │   └── employees/
│   │       └── style.css
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
└── tasks/
    ├── migrations/
    ├── templates/
    │   └── tasks/
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── urls.py
    └── views.py
```

*Your local folder structure may differ slightly. Adjust this tree to match the files in your repository.*

## Getting Started

Follow these steps to run the project locally.

### 1. Prerequisites

Install:
- Python 3.11 or another version compatible with your Django installation
- Git (optional, for cloning the repository)

Check your Python installation:

```bash
python --version
```

### 2. Clone the Repository

Replace the URL below with the actual URL of your GitHub repository.

```bash
git clone https://github.com/Vamsi-Madabathula/django-employee-management-system.git
cd django-employee-management-system
```

### 3. Create and Activate a Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

### 4. Install Django

If the project includes a `requirements.txt` file, install the dependencies with:

```bash
pip install -r requirements.txt
```

If there is no `requirements.txt` file yet, install Django:

```bash
pip install django
```

### 5. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create an Admin Account (Optional)

```bash
python manage.py createsuperuser
```

Follow the prompts to set the username and password.

### 7. Start the Development Server

```bash
python manage.py runserver
```

Open the local development URL in your browser:

- Main application: http://127.0.0.1:8000/
- Django admin: http://127.0.0.1:8000/admin/

Use the actual routes configured in your project if they differ.

## Database Models

### Employee

The Employee model stores employee details, including:
- Name
- Email
- Phone
- Department
- Joining date

### Task

The Task model stores task information, including:
- Title
- Description
- Assigned employee
- Priority
- Status
- Due date

Each task is linked to an employee, allowing tasks to be assigned and tracked.

## Learning Outcomes

This project provides practical experience with:
- Django project and app setup
- URL routing and views
- Models, migrations, and database relationships
- Django ORM and CRUD operations
- Django templates and static CSS files
- Django admin
- Building a structured web application

## Future Enhancements

Planned improvements may include:
- User login and logout
- Role-based access and permissions
- Search and filtering for employees and tasks
- Success/error messages and form validation
- A dashboard with employee and task summaries
- Django REST Framework APIs
- Automated tests and improved documentation

## Screenshots

Add screenshots of your working application here to help visitors understand the interface.

For example, create a `screenshots/` folder in the repository and add images such as:

- `screenshots/employee-list.png`
- `screenshots/employee-form.png`
- `screenshots/task-list.png`

Then embed them in this README:


![Employee List](screenshots/employee_list.png)
![Task List](screenshots/tasks_List.png)

![Employee Management](screenshots/employee_list.png)

## Author

**Vamsi Madabathula**

- GitHub: [Vamsi-Madabathula](https://github.com/Vamsi-Madabathula)

## License

This project is currently provided for learning and portfolio purposes. Add a license file if you decide to distribute it under a specific open-source license.
