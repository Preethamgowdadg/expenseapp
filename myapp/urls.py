# accounts/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('success/', views.success_view, name='success'),
    path('register/', views.register, name='register'),
    path('myapp/details/', views.details_view, name='details'),
     path('myapp/logout/', LogoutView.as_view(next_page='login'), name='logout'), 
     path('myapp/view-details/', views.view_details, name='view_details'),
     path('delete_expense/<int:expense_id>/', views.delete_expense, name='delete_expense'),
]
