from django.shortcuts import render, redirect
from .models import User
import bcrypt
from django.contrib import messages

#RENDER VIEWS:
def index(request):
    context = {
        'users': User.objects.all(),
    }
    return render(request, 'index.html', context)

def success(request):
    context = {
        'users': User.objects.all(),
    }
    return render(request, 'success.html', context)

#REDIRECT VIEWS:
def register(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key,val in errors.items():
                messages.error(request, val, extra_tags=key)
            return redirect('/')
        
        else:
            # assign POST data
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            birthday = request.POST['birthday']
            password = request.POST['password']
            # hash password
            pwhash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

            confirm = request.POST['confirm']
            # create user
            user = User.objects.create(first_name=first_name,last_name=last_name,email=email,birthday=birthday,password=pwhash)
            id = user.id
            request.session['id'] = id
            return redirect('/success')

def login(request):
    pass
