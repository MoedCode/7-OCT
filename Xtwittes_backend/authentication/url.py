from django.urls import path
from . import views
urlpatterns = [
    # path("", views.about , name="about"),
    path("", views.default, name="default"),
    path("home", views.home, name="home"),
    path("signup", views.signup, name="signup"),
]
