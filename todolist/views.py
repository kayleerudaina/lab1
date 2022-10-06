import datetime
from django.shortcuts import render
from todolist.models import TodoItem
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist (request):
    todo_item = TodoItem.objects.filter(user=request.user)
    context = {
    'list_todo': todo_item,
    'nama': 'Kaylee Rudaina Danisha',
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse("todolist:show_todolist"))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def show_create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('deskripsi')
        todo = TodoItem.objects.create(title=title, description=description, date=datetime.date.today(), user=request.user)
        response = HttpResponseRedirect(reverse("todolist:show_todolist"))
        return response
    return render(request, "create.html")

def change(request, pk):
    data = TodoItem.objects.get(id=pk)
    data.is_finished = not(data.is_finished)
    data.save()
    return redirect('todolist:show_todolist')