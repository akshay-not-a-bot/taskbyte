from todo_list_app import views
from django.urls import path

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('delete/<int:task_id>', views.delete_task, name='delete_task'),
    path('edit/<int:task_id>', views.edit_task, name='edit_task'),
    
]
