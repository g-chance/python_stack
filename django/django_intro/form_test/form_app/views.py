from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "index.html")

def create_user(request):
    # if request.method == "GET":
    #     pass
    # if request.method == "POST":
    #     return redirect("/")
    print("Got Post Info....................")
    context = {
    "name_from_form": request.POST['name'],
    "email_from_form": request.POST['email'],
    }
    return redirect("/success")

def success(request):
    return render(request, "success.html")