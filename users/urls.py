from django.urls import path
from setuptools.extern import names

from .views import create_user, user_login, user_logout

urlpatterns = [
    path('users/', create_user, name='create_user'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout')
]
