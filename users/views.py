from django.shortcuts import render, redirect
from . forms import *
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required


def sign_up(request):
    if request.method == 'POST':
        print(request.POST)  # Print POST data for debugging
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(f"User {user.username} created successfully.")
            return redirect('/')
        else:
            print("Form is invalid:", form.errors)  # Debug invalid form
    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'users/signup.html', context)


def login_view(request):  # Renamed the function to login_view
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            print(form.errors)
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            print(user)  # Debugging: Check if user is None
            if user is not None:
                auth.login(request, user)  # Use auth_login to call the login function
                print('login successful')
                return redirect('/')
            else:
                form.add_error(None, 'Invalid username or password')
        else:
            print('form is invalid')
            print(form.errors)
        
    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, 'users/login.html', context)

@login_required(login_url='login')
def user_logout(request):
    auth.logout(request)
    
    return render(request, 'users/logout.html')

@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST or None, instance=request.user)
        P_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.userprofile)
        if u_form.is_valid() and P_form.is_valid():
            u_form.save()
            P_form.save()
            return redirect('profile_link')

    else:
        u_form = UserUpdateForm(instance=request.user)
        P_form = ProfileUpdateForm(instance=request.user.userprofile)

    context = {
        'u_form':u_form,
        'p_form':P_form
    }

    return render(request, 'users/profile.html', context)