# views.py

from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from .serializers import UserSerializer, ProfileSerializer

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        Profile.objects.create(user=user, id_user=user.id)
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
    return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@login_required(login_url='login')
def logout(request):
    auth_logout(request)
    return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def search(request):
    return Response({"message": "Search page"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def about(request):
    return Response({"message": "About page"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def home(request):
    return Response({"message": "Home page"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def default(request):
    return Response({"message": "Default page"}, status=status.HTTP_200_OK)
