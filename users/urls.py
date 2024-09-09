from django.urls import path
from .views import create_user, user_login

urlpatterns = [
    path('users/', create_user, name='create_user'),
    path('login/', user_login, name='user_login'),
]
