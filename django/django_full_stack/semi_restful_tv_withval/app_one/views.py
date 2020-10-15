from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show
from datetime import date
# Create your views here.
def index(request):
    return redirect("/shows")

def shows(request):
    context = {
        "shows": Show.objects.all(),
    }
    return render(request, 'shows.html', context)

def shows_new(request):
    return render(request, "shows_new.html")

def shows_info(request, num):
    context = {
        'show': Show.objects.get(id=num)
    }
    return render(request, "shows_info.html", context)

def shows_edit(request, num):
    context = {
        'show': Show.objects.get(id=num)
    }
    return render(request, "shows_edit.html", context)

def add_show(request):
    errors = Show.objects.basic_validator(request.POST)
    if request.method == "POST":
        request.session['title'] = request.POST['title']
        request.session['network'] = request.POST['network']
        request.session['release_date'] = request.POST['release_date']
        request.session['description'] = request.POST['description']
        if len(errors) > 0:
            for key,value in errors.items():
                messages.error (request,value)
            return redirect('/shows/new')
        else:
            Show.objects.create(title=request.session['title'],network=request.session['network'],release_date=request.session['release_date'],description=request.session['description'])
            num = Show.objects.last().id
            del request.session['title']
            del request.session['network']
            del request.session['release_date']
            del request.session['description']
            return redirect('/shows/'+str(num))

def edit_show(request, num):
    test = Show.objects.get(id=num).title
    errors = Show.objects.basic_validator(request.POST, test)
    if request.method == "POST":
        if len(errors) > 0:
            for key,value in errors.items():
                messages.error (request,value)
            return redirect('/shows/'+str(num)+'/edit')
        else:
            show = Show.objects.get(id=num)
            show.title = request.POST['title']
            show.network = request.POST['network']
            show.release_date = request.POST['release_date']
            show.description = request.POST['description']
            show.save()
            return redirect('/shows/'+str(num))

def delete_show(request, num):
    if request.method == "POST":
        Show.objects.get(id=num).delete()
    if request.method == "GET":
        Show.objects.get(id=num).delete()
    return redirect("/shows")