# authentication/url.py
from django.urls import path
from . import views
from . import api
urlpatterns = [
    path("", views.about , name="about"),
    path("home", views.home, name="home"),
    path("signup", views.signup, name="signup"),
    path("login", views.login, name="login"),
    path("search", views.search, name="search"),
    path('api_signup', api.api_signup, name='api_signup'),
    path("api_login", api.api_login, name="api_login"),
    path("api_logout", api.api_logout, name="api_logout"),
    path("api_logout", api.api_logout, name="api_logout"),
    path("api_search", api.api_search, name="api_search"),
]
