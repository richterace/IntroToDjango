from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "initial/list.html", {"ls":ls})

def home(response):
    return render(response, "initial/home.html", {})
