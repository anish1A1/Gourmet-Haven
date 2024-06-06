from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.contrib.auth.hashers import check_password

def login_user(request):
    if request.method == 'POST':              # If the request method is POST, it means the user is trying to log in.
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)     # Using the authenticate() method to check if the provided credentials are valid.
        
        if user is not None:                 # If authentication is successful, log the user in and redirect to the 'Grocery-Home' page.
            login(request, user)
            return redirect('Grocery-Home')
            # Redirect to a success page.
            
        else:
            messages.error(request, 'Invalid username or password! Please try again.')
            return redirect('login')
        # Return an 'invalid login' error message.  and redirect to the login page
              
    else:              #if user does not want to log in they will just see the login page
        return render(request, 'authenticate/login.html',{})
    
    
def logout_user(request):
    logout(request)               #inbuit method in django
     # Set a message for the user
    messages.success(request, 'You have been logged out!')
    return redirect('Grocery-Home')   


def register_user(request):
    if request.method == 'POST':                  # If the request method is POST, it means the user is submitting the registration form.
        form = RegisterUserForm(request.POST)          #RegisterUserForm is a custom form class that we have defined in our project. we create a forms.py file
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']          # Retrieve the username and password from the form's cleaned data.
            password = form.cleaned_data['password1']
            
            user = authenticate(username= username, password =password)    #to sign them in web application
            login(request, user)         #helps to login also creates a session
            messages.success(request, ('You have been registered successfully!'))
            return redirect('Grocery-Home')
        
    else:
        form = RegisterUserForm()
    return render(request, 'authenticate/register_user.html', {'form': form})


