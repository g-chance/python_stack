from django.shortcuts import render, redirect
from .models import User, Author, Book, Review
from django.contrib import messages
import bcrypt

#RENDER Views:
def index(request):
    
    return render(request, 'index.html')

def books(request):
    if 'userid' not in request.session:
        return redirect('/')
    
    context = {
        'user': User.objects.get(id=request.session['userid']),
        'books': Book.objects.all(),
    }

    return render(request, 'books.html', context)

def booksAdd(request):
    context = {

    }

    return render(request, 'booksAdd.html', context)

def book_info(request, id):
    context = {
        'book': Book.objects.get(id=id)
    }

    return render(request, 'book_info.html', context)

def user_info(request, id):
    count = 0
    for review in User.objects.get(id=id).reviews.all():
        count += 1
    context = {
        'user': User.objects.get(id=id),
        'count': count,
    }

    return render(request, 'user_info.html', context)


#REDIRECT Views:
def register(request):
    errors = User.objects.reg_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
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
        return redirect('/books')

def login(request):
    errors = User.objects.log_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/')
    else:
        user = User.objects.get(email=request.POST['email'])
        request.session['userid'] = user.id
        return redirect('/books')

def add_book(request):
    errors = Book.objects.book_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/books/add')
    else:
        if request.POST['choose_author']:
            author = Author.objects.get(id=id)
        else:
            author = Author.objects.create(
                name = request.POST['author']
            )
        Book.objects.create(
            title=request.POST['title'],
            author=author,
            user=User.objects.get(id=request.session['userid'])
        )
        Review.objects.create(
            rating = request.POST['rating'],
            comment = request.POST['comment'],
            user = User.objects.get(id=request.session['userid']),
            book = Book.objects.last(),
        )
        book = Book.objects.last()
        id = book.id
        return redirect(f'/book_info/{id}')

def add_review(request, id):
    Review.objects.create(
        rating = request.POST['rating'],
        comment = request.POST['comment'],
        user = User.objects.get(id=request.session['userid']),
        book = Book.objects.get(id=id),
    )
    return redirect(f'/book_info/{id}')

def del_review(request, id):
    bookid = Review.objects.get(id=id).book.id
    Review.objects.get(id=id).delete()
    return redirect(f'/book_info/{bookid}')


def logout(request):
    request.session.clear()
    return redirect('/')