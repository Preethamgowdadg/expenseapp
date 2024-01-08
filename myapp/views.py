# accounts/views.py

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth.hashers import check_password
from .forms import CustomUserCreationForm


def login_view(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        try:
            user_data = CustomUser.objects.get(email=email)
            # Now you can access data from the user_data object
            email_ = user_data.email
            password_ = user_data.password
            passwords_match = check_password(password, password_)
            if email == email_ and passwords_match:
                    return success_view(request)
            else:
                message = "Wrong password"
        except CustomUser.DoesNotExist:
            message = "Email ID does not exist. Please register."

        return render(request, 'login.html', {'message': message})
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')

def not_registered(request):
    return render(request, 'not_registered.html')
