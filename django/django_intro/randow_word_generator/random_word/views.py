from django.shortcuts import render, redirect
import random
import string
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['count'] += 1
    return render(request, "index.html")

def generate(request):
    if request.method == "POST":
        if request.POST['whichform'] == "Generate":
            if 'randWord' in request.session:
                del request.session['randWord']
            request.session['randWord'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(14))
            if 'randWord2' in request.session:
                del request.session['randWord2']
            request.session['randWord2'] = get_random_string(length=14)
        if request.POST['whichform'] == "Reset":
            request.session.clear()
    return redirect('/')