from django.db import models
import re
import bcrypt

#Managers
class UserManager(models.Manager):
    def reg_validator(self, post):
        errors = {}
        if len(post['first_name']) < 2:
            errors['first_name'] = "Your first name must be at least 2 characters"
        if len(post['last_name']) < 2:
            errors['last_name'] = "Your last name must be at least 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post['email']):
            errors['email'] = "Invalid Email address"
        if len(User.objects.filter(email=post['email'])) > 0:
            errors['email'] = "Email already taken"
        if len(post['password']) < 8:
            errors['reg_pw'] = "Your password should be at least 8 characters"
        if post['password'] != post['confirm_password']:
            errors['confirm_pw'] = "Passwords do not match"
        return errors
    
    def log_validator(self, post):
        errors = {}
        if len(User.objects.filter(email=post['email'])) == 0:
            errors['login_em'] = "Invalid email"
        else:
            user = User.objects.get(email=post['email'])
            if not bcrypt.checkpw(post['password'].encode(), user.password.encode()):
                errors['login_pw'] = "Incorrect email/password combination"
        return errors

class BookManager(models.Manager):
    def book_validator(self, post):
        errors = {}
        if len(post['title']) < 1:
            errors['title'] = "Book must have a title"
        if len(Book.objects.filter(title=post['title'])) > 0:
            errors['title'] = "Title must be unique"
        if len(post['author']) < 1:
            errors['author'] = "Book must have an author"
        if len(post['comment']) > 0 and len(post['comment']) < 10:
            errors['comment'] = "Comments must be at least 10 characters"
        return errors

#Models
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #books
    #reviews
    objects = UserManager()

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #books


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #reviews
    objects = BookManager()

class Review(models.Model):
    rating = models.IntegerField()
    comment = models.TextField()
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
