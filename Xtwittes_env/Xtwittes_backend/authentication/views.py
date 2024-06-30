from django.shortcuts import render
from django.http import  HttpResponse, JsonResponse
# Create your views here.

def about(request):
    return render(request, "about.html")
def index(request):
    return render(request, "signin.html")
