
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from user.forms import Userform, Usereditform
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login , logout
from shop.views import store_index
from cart.models import Cart
# Create your views here.
def index(request):
    user = User.objects.all() 
    context={
        "user":user,
    }
    return render(request, "user/index.html",context)

@login_required(login_url="/user/join/login")
def details (request,id):
    user =get_object_or_404(User,id=id)
    context={
        "user":user,
    }
    return render(request, "user/details.html",context)


@login_required(login_url="/user/join/login")
def delete(request, id):
    user =get_object_or_404(User,id=id)
    cart = get_object_or_404(Cart,User=user)
    
    cart.delete()
    user.delete()
    return redirect(index)


def add(request):
    form=Userform(request.POST or None)

    if form.is_valid():
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
       
       
        user =  User.objects.create_user(username, email, password )
        user.first_name=request.POST['first_name']
        user.last_name=request.POST['last_name']
        
        user.save()

        cart = Cart()
        cart.User=user
        cart.save()

    context={
        "form": form,
    }
    return render(request, "user/add.html", context)

@login_required(login_url="/user/join/login")
def edit(request, id):
    user=get_object_or_404(User, id=id)
    form=Usereditform(request.POST or None, instance=user)

    if form.is_valid():
       
        user.email=request.POST['email']
        user.first_name=request.POST['first_name']
        user.last_name=request.POST['last_name']
        
        user.save()
        return redirect(index)

    context={
        "form": form,
    }
    return render(request, "user/edit.html",context) 

def back_to_list(request):

    return redirect(index)

def userlogin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user =authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect(index)

    return render(request, "user/login.html")

def userlogout(request):
     logout(request)   
     return redirect(store_index)
