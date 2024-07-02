from django.shortcuts import (render, redirect)
from django.http import  (HttpResponse, JsonResponse)
from django.contrib import messages
from django.contrib.auth.models import (User,  auth)
from .models import Profile
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

#                      Signup
def signup(request):
    """rout a signup page .. register and save a new user creates a  user profile """

    # receiving user data from request in a dictionary
    if request.method == "POST":
        duser = {
            "username": request.POST["username"],
            "email": request.POST["email"],
            "password": request.POST["password"],

        }

        # validating user data
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
                # profile
                user_query = User.objects.filter(email=duser["email"]).first()
                ''' START_DEBUG  '''
                x = user_query.__dict__
                helper.log_f(x)
                ''' END_DEBUG'''
                user_profile = Profile.objects.create(user=user_query, id_user=user_query.id)
                user_profile.save()
                # render  profile page
                return redirect("signup")
        else:

            messages.info(request, "Password  Not Match")
            return redirect("signup")
    return render(request, "signup.html")

def login(request):
    return render(request, "login.html")