from django.shortcuts import render, redirect
from .models import Description, Course, Comment
from django.contrib import messages

# Create your views here.

## RENDER:
def index(request):
    context = {
        'courses': Course.objects.all(),
    }
    return render(request, 'index.html', context)

def courses_destroy_id(request, id):
    context = {
        'course': Course.objects.get(id=id),
    }
    return render(request, 'destroy.html', context)

def courses_comment_id(request, id):
    context = {
        'course': Course.objects.get(id=id),
        'comments': Course.objects.get(id=id).comments.all()
    }
    return render(request, 'comments.html', context)

## REDIRECT:
def add_course(request):
    if request.method == "POST":
        errors = Course.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            request.session.clear()
            name = request.POST['name']
            desc = request.POST['desc']
            # name = request.session['name']
            # desc = request.session['desc']
            course = Course.objects.create(name=name)
            Description.objects.create(content=desc,course=course)
            # Course.objects.last().description.add(Description.objects.last())
            # Description.objects.create(content=desc)
            return redirect('/')

def destroy_course(request, id):
    Course.objects.get(id=id).delete()
    return redirect('/')

def add_comment(request,id):
    if request.method == 'POST':
        comment = request.POST['comment']
        Course.objects.get(id=id).comments.create(content = comment)
        return redirect('/courses/comment/'+str(id))

def destroy_comment(request, id, course):
    if request.method == 'POST':
        Comment.objects.get(id=id).delete()
        return redirect('/courses/comment/'+str(course))