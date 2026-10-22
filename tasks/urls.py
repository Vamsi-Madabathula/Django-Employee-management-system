from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks_list, name= 'tasks_list'),# name is used to call the task_list () at html file
    path('add/',views.task_create, name = 'task_create'),
    path('update/<int:id>/',views.task_update, name = 'task_update'),
    path('deletesss/<int:id>/',views.task_delete, name = 'task_delete')
]