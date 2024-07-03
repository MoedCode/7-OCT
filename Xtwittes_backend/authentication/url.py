from django.urls import path
from . import views
urlpatterns = [
    path("", views.about , name="about"),
    path("home", views.home, name="home"),
    path("signup", views.signup, name="signup"),
    path("login", views.login, name="login"),
    path("search", views.search, name="search"),
]
