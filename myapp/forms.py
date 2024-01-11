# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,Expense

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['date', 'amount', 'mode', 'reason', 'number']

    def save(self, commit=True):
        instance = super().save(commit=False)
        user_email = self.initial.get('user_email', None)
        
        if user_email:
            user_data = CustomUser.objects.get(email=user_email)
            instance.number = user_data.id

        if commit:
            instance.save()

        return instance

