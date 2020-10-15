from django.shortcuts import render, redirect
from .models import User, Book
from django.contrib import messages
import bcrypt
# Create your views here.
#RENDER VIEWS:
def index(request):
    context = {

    }
    return render(request, 'index.html', context)

def books_dash(request):
    if 'userid' not in request.session:
        return redirect('/')

    context = {
        'user': User.objects.get(id=request.session['userid']),
        'books': Book.objects.all(),
        'liked_books': Book.objects.filter(favorite_users = User.objects.get(id=request.session['userid'])),
    }
    return render(request, 'books_dash.html', context)

def book_info(request, id):
    context = {
        'book': Book.objects.get(id=id),
        'liked_users': User.objects.filter(favorite_books = Book.objects.get(id=id))
    }
    return render(request, 'books_info.html', context)

#REDIRECT VIEWS:
def register(request):
    errors = User.objects.reg_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        User.objects.create (
            first_name= request.POST['first_name'],
            last_name= request.POST['last_name'],
            email= request.POST['email'],
            password= pw_hash,
        )
        user = User.objects.last()
        request.session['userid'] = user.id
    return redirect('/books_dash')

def login(request):
    errors = User.objects.log_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/')
    else:
        user = User.objects.get(email=request.POST['login_em'])
        request.session['userid'] = user.id
        return redirect('/books_dash')

def add_book(request):
    errors = Book.objects.book_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/books_dash')
    else:
        Book.objects.create(
            title= request.POST['title'],
            description= request.POST['description'],
            added_user= User.objects.get(id=request.session['userid']),
        )
        book = Book.objects.last()
        book.favorite_users.add(User.objects.get(id=request.session['userid']))
        # request.session['bookid'] = book.id
        id = book.id
        return redirect(f"/book_info/{id}")

def add_favorite(request, id):
    Book.objects.get(id=id).favorite_users.add(User.objects.get(id=request.session['userid']))

    return redirect('/books_dash')

def edit_book(request, id):
    errors = Book.objects.book_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect(f'/book_info/{id}')
    else:
        book = Book.objects.get(id=id)
        book.title = request.POST['title']
        book.description = request.POST['description']
        book.save()
        return redirect(f'/book_info/{id}')

def delete_book(request,id):
    Book.objects.get(id=id).delete()
    return redirect('/books_dash')

def logout(request):
    request.session.clear()
    return redirect('/')