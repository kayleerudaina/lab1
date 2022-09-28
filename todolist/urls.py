from django.urls import path
from todolist.views import show_todolist, register, login_user, logout_user,show_create_task

# TODO: Implement Routings Here
app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name = 'show_todolist'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('create-task/', show_create_task, name='create_task'),
    path('logout/', logout_user, name='logout'),
]