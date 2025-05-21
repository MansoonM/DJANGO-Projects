from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=="POST":
        username= request.POST["username"]
        password= request.POST["password"]
        user= User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, "Account Registerd Sucessfully!")
        return redirect("login")
    return render(request, "register.html")



def user_login(request):
    if request.method=="POST":
        username= request.POST["username"]
        password= request.POST["password"]
        user= authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "home.html")
        else:
            messages.error(request,"Unsucessful")
    return render(request,"login.html")

def user_logout(request):
    logout(request)
    return redirect('login')
