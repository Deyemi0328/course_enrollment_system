from django.urls import path
from .views import Register_view, login_view, logout_view, homePage_view


urlpatterns = [
    path('register/', Register_view, name = 'register'),
    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name ='logout'),
    path('homepage/', homePage_view, name = 'homepage')
]