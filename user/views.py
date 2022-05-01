
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from user.forms import Userform

# Create your views here.
def index(request):
    user = User.objects.all() 
    context={
        "user":user,
    }
    return render(request, "user/index.html",context)

def details (request,id):
    user =get_object_or_404(User,id=id)
    context={
        "user":user,
    }
    return render(request, "user/details.html",context)

def delete(request, id):
    user =get_object_or_404(User,id=id)
    user.delete()
    return redirect(index)

def add(request):
    form=Userform(request.POST or None)

    if form.is_valid():
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']

        user =  User.objects.create_user(username, password, email)
        user.save()

    context={
        "form": form,
    }
    return render(request, "user/add.html", context)

def edit(request, id):
    context={}
    return render(request, "user/edit.html",context) 

def back_to_list(request):

    return redirect("user/index.html")


