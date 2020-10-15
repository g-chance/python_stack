from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.
def index(request):
    context = {
        "books": Book.objects.all()
    }
    return render(request, "index.html", context)

def add_book(request):
    if request.method == "POST":
        title = request.POST["title"]
        desc = request.POST["desc"]
        Book.objects.create(title = title, desc = desc)
    return redirect("/")

def add_author(request):
    if request.method == "POST":
        f_n = request.POST["f_n"]
        l_n = request.POST["l_n"]
        Author.objects.create(first_name = f_n, last_name = l_n)
    return redirect("/author")

def add_author_to_book(request, num):
    if request.method == "POST":
        selectauth = request.POST['selectauth']
        Book.objects.get(id=num).authors.add(Author.objects.get(id=selectauth))
    return redirect('/books/'+str(num))

def add_book_to_author(request, num):
    if request.method == "POST":
        selectbook = request.POST['selectbook']
        Author.objects.get(id=num).books.add(Book.objects.get(id=selectbook))
    return redirect('/author_info/'+str(num))

def books(request, num):
    context = {
        "book": Book.objects.get(id=num),
        "authors": Author.objects.exclude(books = Book.objects.get(id=num)),
    }
    return render(request, "books.html", context)

def author_info(request, num):
    context = {
        "author": Author.objects.get(id=num),
        'books': Book.objects.exclude(authors = Author.objects.get(id=num))
    }
    return render(request, "author_info.html", context)

def author(request):
    context = {
        "authors": Author.objects.all()
    }
    return render(request, "authors.html", context)

def home(request):
    return redirect("/")