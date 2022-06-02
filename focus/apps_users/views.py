from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):
    """ Register a new user """
    if (request.method == "POST"):
        firstname, lastname, username = request.POST['firstname'], request.POST['lastname'], request.POST['username']
        contact, email = request.POST['contact'], request.POST['email']
        password, repeated_password = request.POST['password'], request.POST['repeatpassword']

        if firstname is None:
            messages.info(request, "Enter first name")
            return redirect("register")

        if password == repeated_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists!')
                return redirect("register")
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists!')
                return redirect("register")
            if User.objects.filter(contact=contact).exists():
                messages.info(request, 'Contact already exists!')
                return redirect("register")

            user = User.objects.create_user(
                firstname=firstname,
                lastname =lastname,
                username=username,
                contact=contact,
                email=email,
                password=password
            )
            user.save()
            return redirect(request, "login")

        else:
            messages.info(request, "Passwords are not the same!")
            return redirect("register")
    elif (request.method == "GET"):
        return render(request, 'register.html')

def login(request):
    """ Log in a user """
    
    if (request.method == "POST"):
        pass