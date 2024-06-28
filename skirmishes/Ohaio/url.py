from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # Corrected from "/" to ""
    path("trash", views.index1, name="index1"),
    path("<str:name>", views.great, name="great"),
    path("useless/<str:text>/<str:number>", views.useless, name="useless"),


]