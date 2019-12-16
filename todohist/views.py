from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.

def ToDoHistory(request):
    return render (request, 'todohist.html')
