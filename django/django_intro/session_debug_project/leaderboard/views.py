from django.shortcuts import render, redirect

# Create your views here.
def index(request): 

    return render(request, "index.html")


def leaderBoard(request):

    if "user_name" not in request.session:
        print('redirecting...')
        return redirect('/')
    
    ranks = ["first", "second", "third"]

    for key in ranks:
        if key not in request.session:
            request.session[key] = 'Please assign a rank.'

    return render(request, "leaderboard.html")

def show(request, rank):

    name = ""

    if rank == 1:
        if request.session['first'] == "Please assign a rank.":
            return redirect('/leaderboard')
        name = request.session['first']
    elif rank == 2:
        if request.session['second'] == "Please assign a rank.":
            return redirect('/leaderboard')
        name = request.session['second']
    else:
        if request.session['third'] == "Please assign a rank.":
            return redirect('/leaderboard')
        name = request.session['third']

    return render(request, "showFriend.html", {'rank':rank, 'name': name })

def enter(request):
    print(request.POST)
    name = request.POST["first_name"] + " " + request.POST["last_name"]
    request.session['user_name'] = name
    return redirect('/leaderboard')

def changeRanks(request):

    print(request.POST)

    if request.POST['first'] != '':
            request.session['first'] = request.POST['first']
    if request.POST['second'] != '':
            request.session['second'] = request.POST['second']
    if request.POST['third'] != '':
            request.session['third'] = request.POST['third']

    return redirect('/leaderboard')

def logout(request):
    request.session.clear()
    return redirect('/')