# myapp/forms.py
from django import forms
from .models import LoginAdmin

class LoginForm(forms.ModelForm):
    class Meta:
        model = LoginAdmin
        fields = ['username', 'password']  # We only need username and password for login
    
    # Optionally, add custom validation if needed
    def clean_password(self):
        password = self.cleaned_data.get('password')
        # You can implement any password validation here
        return password
