from django.shortcuts import render, redirect
import random

# Create your views here.

def index(request):
    if 'playturns' not in request.session:
        request.session['playturns'] = None
    if 'playgolds' not in request.session:
        request.session['playgolds'] = None
    if 'totalgold' not in request.session:
        request.session['totalgold'] = 0
    if "activity" not in request.session:
        request.session["activity"] = ""
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['count'] += 1
    # if request.session['playturns'] == True:
    #     if count == 5:
    #         win = False
    #     elif request.session['totalgold'] >= 100:
    #         win == True
    if request.session['playgolds'] == True:
        request.session['win'] = None
        print("IN INDEX ROUTE", request.session['win'])
        if request.session['totalgold'] <= 0:
            request.session['win'] = True
    if request.session['playturns'] == True:
        request.session['win'] = None
        print("IN INDEX ROUTE", request.session['win'])
        if request.session['totalgold'] >= 100:
            request.session['win'] = True
        elif request.session['count'] > 5:
            request.session['win'] = False

    return render(request, 'index.html')

def home(request):
    return render(request, "home.html")

def play(request):
    if request.method == "POST":
        if request.POST["huh?"] == "turns":
            request.session['playturns'] = True
            request.session['totalgold'] = 0
        if request.POST["huh?"] == "golds":
            request.session['playgolds'] = True
            print("IN PLAY ROUTE", request.session['playgolds'])
            request.session['totalgold'] = 50
    return redirect("/")

def process(request):
    if request.method == "POST":
        totalgold = request.session["totalgold"]
        if request.POST["whoami"] == "farm":
            farm = random.randint(10,20)
            request.session["totalgold"] += farm
        if request.POST["whoami"] == "cave":
            cave = random.randint(5,10)
            request.session["totalgold"] += cave
        if request.POST["whoami"] == "house":
            house = random.randint(2,5)
            request.session["totalgold"] += house
        if request.POST["whoami"] == "casino":
            casino = random.randint(-50,50)
            request.session["totalgold"] += casino
        if request.session["totalgold"]-totalgold > 0:
            request.session["activity"] += "<p class='earn'>You have earned "+str(request.session["totalgold"]-totalgold)+" gold</p>"
        else:
            request.session["activity"] += "<p class='lose'>You have lost "+str((request.session["totalgold"]-totalgold)*-1)+" gold</p>"
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/home')