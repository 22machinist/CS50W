from django.shortcuts import render
from .models import * 

#Creating views

def menu(request) :
    items = MenuItem.objects.all()
    dishes = MenuDish.objects.all()
    context = {
        "items" : items ,
        "dishes" : dishes 
    }
    return render(request , "menu/menu.html" , context)