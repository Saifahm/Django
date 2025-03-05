# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.http import HttpResponse

def home_view(request):
    return render(request,'home.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Authenticate the user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # If authentication is successful, log the user in
                login(request, user)
                return redirect('/')  # Redirect to the homepage or a success page
            else:
                return HttpResponse("Invalid credentials, please try again.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
