from django.urls import path
from .views import signup, login, logout, search, about, home, default

urlpatterns = [
    path('api/signup/', signup, name='api_signup'),
    path('api/login/', login, name='api_login'),
    path('api/logout/', logout, name='api_logout'),
    path('api/search/', search, name='api_search'),
    path('api/about/', about, name='api_about'),
    path('api/home/', home, name='api_home'),
    path('api/default/', default, name='api_default'),
]
