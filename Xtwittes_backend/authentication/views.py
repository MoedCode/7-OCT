from django.shortcuts import (render, redirect)
from django.http import  (HttpResponse, JsonResponse)
from django.contrib import messages
from django.contrib.auth.models import User

# from helper import *
from . import helper
# Create your views here.
""" here all controllers function for authentication app
    Until further notice
"""


def about(request):
    """ about"""
    return render(request, "about.html")


def default(request):
    """ default"""
    return render(request, "signin.html")


def home(request):
    """ home"""


    return render(request, "index.html")


def signup(request):
    """signup"""
    if request.method == "POST":
        duser = {
            "username": request.POST["username"],
            "email": request.POST["email"],
            "password": request.POST["password"],

        }

        if duser["password"] == request.POST["password2"]:
            if User.objects.filter(email=duser["email"]).exists():
                messages.info(request, f"{duser['email']} is already exist ")
                return redirect("signup")
            if User.objects.filter(email=duser["username"]).exists():
                messages.info(request, f"{duser['username']} is already exist ")
                return redirect("signup")
            else:
                user_obj = User.objects.create_user(**duser)
                user_obj.save()
                tst = User.objects.filter(email=duser["email"]).first()
                x = tst.__dict__
                helper.log_f(x)
                print(x)
                return render(request, "subprof.html", {"email":x["email"],"username":x["username"]})

        else:

            messages.info(request, "Password  Not Match")
            return redirect("signup")

    return render(request, "signup.html")