# from django.shortcuts import render
# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistrationForm

# Create your views here.

# def account_list(request):
#    return  HttpResponse('<h1>Account list</h1>')

# def account_update(request):
#     return  HttpResponse(f'<h1>Update account</h1>')

# def account_create(request):
#     return  HttpResponse(f'<h1>Create account</h1>')

# def account_delete(request):
#     return  HttpResponse(f'<h1>Delete account</h1>')

# def account_details(request):
#     return  HttpResponse(f'<h1>Account details</h1>')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('trainee_list')
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'account/register.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')