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
from django.urls import path
from django.conf.urls import include
from django.contrib.auth.models import User
from todo.views import ToDoView, AddToDo, DeleteToDo, ToDoHistView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', ToDoView),
    path('todohist/', ToDoHistView),

    # Retrieves the post from todo.html
    path('addtodo/', AddToDo), # Calls the AddToDo method in views.py
    path('deletetodo/<int:todo_id>/', DeleteToDo), # Calls the DeleteToDo method in views.py and passes the todo_id from todo.html

    # Login
    path('accounts/', include('django.contrib.auth.urls')),
]

# Creating a test user account
# # Create user and save to the database
# User.objects.filter(username = 'myusername').delete()
# user = User.objects.create_user('myusername', 'myemail@gmail.com', 'mypassword')

# # Update fields and then save again
# user.first_name = 'John'
# user.last_name = 'Lim'
# user.save()