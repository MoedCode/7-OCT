from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # Corrected from "/" to ""
    path("trash", views.index1, name="index1"),
    path("<str:name>", views.great, name="great"),
    path("<str:text>/<int:number>", views.useless, name="useless"),
    path("<str:text>/<int:number>", views.useless2, name="useless2")
]