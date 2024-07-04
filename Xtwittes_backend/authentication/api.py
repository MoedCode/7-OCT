from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import Profile
from . import helper

# About
def api_about(request):
    return JsonResponse({'message': 'This is the about page'})

# Signup
def api_signup(request):
    if request.method == "POST":
        duser = {
            "username": request.POST["username"],
            "email": request.POST["email"],
            "password": request.POST["password"],
        }

        if duser["password"] == request.POST["password2"]:
            if User.objects.filter(email=duser["email"]).exists():
                return JsonResponse({'error': f"{duser['email']} is already taken"})
            if User.objects.filter(username=duser["username"]).exists():
                return JsonResponse({'error': f"{duser['username']} is already taken"})
            else:
                user_obj = User.objects.create_user(**duser)
                user_profile = Profile.objects.create(user=user_obj, id_user=user_obj.id)
                return JsonResponse({'success': 'User created successfully'})
        else:
            return JsonResponse({'error': 'Passwords do not match'})
    else:
        return JsonResponse({'error': 'Method not allowed'})

# Login
def api_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'error': 'Invalid credentials'})
    else:
        return JsonResponse({'error': 'Method not allowed'})

# Logout
@login_required(login_url='signin')
def api_logout(request):
    auth.logout(request)
    return JsonResponse({'message': 'Logged out successfully'})

# Search
def api_search(request):
    return JsonResponse({'message': 'Search page'})
