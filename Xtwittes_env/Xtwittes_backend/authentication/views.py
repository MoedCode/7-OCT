from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.

def index(request):
    return render(request, "/mnt/c/Users/Active/Desktop/Coding/Short_Specializations/Portfolio_project/Xtwittes/Xtwittes_env/templates/index.html")