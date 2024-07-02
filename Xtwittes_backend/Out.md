------helper.py-------------
def assign_id(obj: object, id_type: int = 4, key_name: str = None) -> str:
    """Assigns a unique identifier (UUID) to an object based on the specified type."""
    import uuid

    if id_type == 5:
        key = key_name if key_name else getattr(obj, "username", None)
        if not key:
            raise KeyError(
                "Object must have an attribute 'username' or a valid 'key_name' must be provided.")
        return str(uuid.uuid5(uuid.NAMESPACE_DNS, key))

    if id_type == 1:
        return str(uuid.uuid1())

    elif id_type == 3:
        key = key_name if key_name else getattr(obj, "username", None)
        if not key:
            raise KeyError(
                "Object must have an attribute 'username' or a valid 'key_name' must be provided.")
        return str(uuid.uuid3(uuid.NAMESPACE_DNS, key))

    else:
        return str(uuid.uuid4())


def current_time(to_str: bool = True):
    from datetime import datetime
    """
    Return the current time. If to_str is True, return the time formatted as '%Y-%m-%dT%H:%M:%S.%f'.
    Otherwise, return the datetime object.
    """
    current_time = datetime.now()
    if to_str:
        formatted_time = current_time.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return formatted_time
    else:
        return current_time


def log_f(data: any, dtype: str, file_name: str = "log.md", timing: bool = False) -> None:
    """ log message to console  """
    with open('log.md', 'a') as FILE:
        FILE.write(f'```{dtype}\n')
        if timing:
            from datetime import datetime
            FILE.write(f'{current_time()}')
        FILE.write(f'{data}\n')
        FILE.write('```\n')
------view.py-------------
from django.shortcuts import (render, redirect)
from django.http import  (HttpResponse, JsonResponse)
from django.contrib import messages
from django.contrib.auth.models import User

from helper import *
# import helper
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
            "password2": request.POST["password2"],
        }

        if duser["password"] == duser["password2"]:
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
                helper.log_f(tst.__dict__)


        else:
            messages.info(request, "Password  Not Match")
            return redirect("signup")

    return render(request, "signup.html")