from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
str = ''' <h1>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Necessitatibus
alias odio, id, voluptas accusantium eos vero labore cumque nihil quod ipsa et omnis
voluptatem accusamus tenetur consequatur deserunt quas in.</h1>'''
def index(request):
    return render(request, "index.html")
def index1(request):
    return HttpResponse(str)
def great(request, name):
    return HttpResponse( f"<h1> Hello , {name} </h1> {request.__dict__}")
def useless(request, text, number):
    return render(request, "useless.html",{
        "text":text, "number":number
    })
