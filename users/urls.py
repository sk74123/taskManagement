from django.urls import path

from .views import create_user, test_greeting

urlpatterns = [
    path('users/', create_user, name='create_user'),
    path('greeting/', test_greeting, name='test_greeting'),
]
