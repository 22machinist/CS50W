from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User

import datetime
from annoying.functions import get_object_or_None 
from django.contrib.auth.decorators import login_required 

from .models import * 

#This is the default view 
def index(request):
    return render(request , "auctions/index.html")


#This is the view for the login
def login_view(request) :
    if request.method == "POST" :
        #Attempt to sign user in 
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username , password=password)
        #Checking for the valid authentication
        if user is not None :
            login(request , user)
            return HttpResponseRedirect(reverse("index"))
        #If authentication is not valid 
        else :
            return render(request , "auctions/login.html" , {
                "message": "Invalid username or password" , 
                "msg_type" : "danger" 
            })
            
    #If get the request 
    else : 
        return render(request, "auctions/login.html")
    
    
#View for logging out 
def logout_view(request) :
    logout(request)
    return HttpResponseRedirect(reverse("index"))


#View for registering 
def register(request):
    if request.method == "POST" :
        username = request.POST["username"]
        email = request.POST["email"]
        #Ensuring that password matches the confirmation 
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation : 
            return render(request, "auction/register.html" , {
                "message" : "Password not match", 
                "msg_type" : "danger"
            })
            
        if not username :
            return render(request , "auctions/register.html" , {
                "message" : "Please Enter Your Valid Username ." , 
                "msg_type" : "danger"
            })
            
        if not email :
            return render(request , "auctions/register.html" , {
                "message" : "Please Enter Your Valid Email" , 
                "msg_type" : "danger"
            })
        #Attempting to create the new user 
        try : 
            user = User.objects.create_user(username , email , password)
            user.save() 
        except IntegrityError : 
            return render(request , "auctions/register.html" , {
                "message" : "Username is already in use." , 
                "msg_type" : "danger"
            })
        login(request , user)
        return HttpResponseRedirect(reverse("index"))
    
    #if GET request 
    else : 
        return render (request , "auctions/register.html")
    
#View for the dashboard 
@login_required(login_url='/login')
def dashboard(request) :
    winners = Winner.objects.filter(winner=request.user.username)
    #Checking for watchlist 
    lst = Watchlist.objects.filter(user=request.user.username)
    #List of the products available in the WinnerModel
    present = False 
    prodlst = []
    i = 0 
    if lst :
        present = True 
        for item in lst :
            product = Listing.objects.get(id=item.listingid)
            prodlst.append(product)
    print(prodlst)
    return render(request , "auctions/dashboard.html" , {
        "products" : products , 
        "empty" : empty
    })
    
#View to create the listing 
