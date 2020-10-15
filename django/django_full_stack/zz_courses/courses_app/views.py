from django.shortcuts import render, redirect
from .models import Course
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'index.html', context)

def add_course(request):
    if request.method == "POST":
        errors = Course.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            name = request.POST['name']
            desc = request.POST['desc']
            Course.objects.create(name=name,desc=desc)
            return redirect('/')

def courses_destroy_int(request, id):
    context = {
        'course': Course.objects.get(id=id)
    }
    return render(request, 'destroy.html', context)

def destroy_course(request, id):
    if request.method == "POST":
        Course.objects.get(id=id).delete()
        return redirect('/')
