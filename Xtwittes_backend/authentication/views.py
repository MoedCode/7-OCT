from django.shortcuts import render
from django.http import  HttpResponse, JsonResponse
# Create your views here.

def about(request):
    return render(request, "about.html")
def default(request):
    return render(request, "signin.html")
def home(request):
    return render(request, "index.html")
