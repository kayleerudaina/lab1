from django.urls import path
from todolist.views import show_todolist, register, login_user, logout_user,show_create_task, change, delete, show_json, add_todo_ajax

# TODO: Implement Routings Here
app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name = 'show_todolist'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('create-task/', show_create_task, name='create_task'),
    path('delete/<int:pk>', delete, name='delete'),
    path('change/<int:pk>', change, name='change'),
    path('json/', show_json, name='show_json'),
    path('add/', add_todo_ajax, name='add_todo_ajax')
]