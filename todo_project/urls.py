"""todo_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from todo.views import ToDoView, AddToDo, DeleteToDo, ToDoHistView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Contributions View page
def ContributionsView(request):
    return render(request, 'contributions.html')

# Sign Up page
def SignUpView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = User.objects.create_user(username, 'anemail@gmail.com', raw_password)
            user.save()
            return redirect('todo')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', ToDoView, name='todo'),
    path('todohist/', ToDoHistView, name='todohist'),

    # Retrieves the post from todo.html
    path('addtodo/', AddToDo), # Calls the AddToDo method in views.py
    path('deletetodo/<int:todo_id>/', DeleteToDo), # Calls the DeleteToDo method in views.py and passes the todo_id from todo.html

    # Login & Signup
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', SignUpView, name='signup'),

    path('contributions/', ContributionsView)
]

'''
# Creating a test user account
# Create user and save to the database
User.objects.filter(username = 'myusername').delete()
user = User.objects.create_user('myusername', 'myemail@gmail.com', 'mypassword')	

# Update fields and then save again
user.first_name = 'John'
user.last_name = 'Lim'
user.save()
'''
