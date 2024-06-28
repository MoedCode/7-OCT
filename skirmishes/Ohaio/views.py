from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "Ohaio/index.html")
def index1(request):
    return render(request, "Ohaio/index1.html")
def great(request, name):
    return HttpResponse( f"<h1> Hello , {name} </h1> {request.__dict__}")
def useless(request, text, number):
    x = list(range(int(number)))
    return render(request, "Ohaio/useless.html",{"text":text, "number":int(number), 'N':x}
    )
