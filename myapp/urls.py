# accounts/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('success/', views.success_view, name='success'),
    path('register/', views.register, name='register')
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # Add more authentication URLs as needed
]
