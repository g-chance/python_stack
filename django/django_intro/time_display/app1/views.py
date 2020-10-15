from django.shortcuts import render, redirect
from time import strftime, gmtime, time

def index(request):
    context = {
        "datetime": strftime("%A %B %d, %Y -- %I:%M %p", gmtime()),
        "testtime": gmtime(time()),
    }
    return render(request, "index.html", context)

def time_display(request):
    context = {
        "datetime": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request, "index.html", context)

# Create your views here.
