from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

# RENDER:
def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'index.html', context)

def success(request, id):
    if 'email' not in request.session:
        return redirect('/')
    else:
        context = {
            'users': User.objects.all(),
            'user': User.objects.get(id=id),
        }
        return render(request, 'success.html', context)

#REDIRECT:
def register(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, val in errors.items():
                messages.error(request, val, extra_tags=key)
            return redirect('/')
        else:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']

            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()

            User.objects.create(first_name=first_name,last_name=last_name,email=email,password=pw_hash)
            id = User.objects.last().id
            return redirect('/success/'+str(id))

def login(request):
    if request.method == "POST":
        errors = User.objects.validate_login(request.POST)
        if len(errors) > 0:
            for key,val in errors.items():
                messages.error(request, val)
            return redirect('/')
        else:
            user = User.objects.get(email=request.POST['email'])
            id = user.id
            request.session['email'] = user.email
            return redirect('/success/'+str(id))
        pass

def logout(request):
    del request.session['email']
    return redirect('/')