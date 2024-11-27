# from django.http import HttpResponse
# from django.template import loader
# from django.shortcuts import render,redirect
# from django.contrib.auth import authenticate,login,logout
# from django.contrib import messages
# from .forms import LoginFortm, Signupform
# from .models import UserProfile
# from django.contrib.auth.models import user

def home(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())
def about(request):
    template=loader.get_template('about.html')
    return HttpResponse(template.render())

def contact(request):
    template=loader.get_template('contact.html')
    return HttpResponse(template.render())
def login(request):
    template=loader.get_template('login.html')
    return HttpResponse(template.render())
def register(request):
    template=loader.get_template('register.html')
    return HttpResponse(template.render())



from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

def register_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Create a new user with a hashed password
        user = User.objects.create(username=username, email=email, password=make_password(password))
        return redirect('login_page')  # Redirect to the login page

    return render(request, 'register.html')
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.shortcuts import redirect

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Log the user in and redirect
            login(request, user)
            return redirect('index')  # Replace 'home' with your target view name
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login_page')
