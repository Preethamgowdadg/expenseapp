# accounts/views.py

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import CustomUser,Expense
from django.contrib.auth.hashers import check_password
from .forms import CustomUserCreationForm,ExpenseForm
from django.contrib.auth.views import LogoutView


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
                    request.session['user_email'] = email
                    return redirect('details')
                    # return success_view(request)
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



def details_view(request):
    user_email = request.session.get('user_email', None)
    user_data = CustomUser.objects.get(email=user_email)
    print('++++++==',user_data)
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details')
            # You might want to add a success message or redirect to another page
    else:
        form = ExpenseForm()

    return render(request, 'details.html', {'form': form,'user_data':user_data})


logout_view = LogoutView.as_view(next_page='login')


def view_details(request):
    expenses = Expense.objects.all()
    return render(request, 'view_details.html', {'expenses': expenses})