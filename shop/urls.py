from django.urls import path, include
from .views import helloworld, about_us, login_user, logout_user

urlpatterns = [
    path('', helloworld, name='home'),
    path('about/', about_us, name='about'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
