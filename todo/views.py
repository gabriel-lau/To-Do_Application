from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDoItem

# Methods to interact the interface with the backend
def ToDoView(request):
    todo_items = ToDoItem.objects.all()
    return render(request, 'todo.html', {'all_items': todo_items})

def AddToDo(request):
    new_item = ToDoItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')

def DeleteToDo(request, todo_id):
    delete_item = ToDoItem.objects.get(id = todo_id)
    delete_item.delete()
    return HttpResponseRedirect('/todo/')

