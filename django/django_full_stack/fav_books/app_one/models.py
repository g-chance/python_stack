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
            errors['password'] = "Your password should be at least 8 characters"
        if post['password'] != post['confirm_password']:
            errors['confirm_password'] = "Passwords do not match"
        return errors
    
    def log_validator(self, post):
        errors = {}
        if len(User.objects.filter(email=post['login_em'])) == 0:
            errors['login_em'] = "Invalid email"
        else:
            user = User.objects.get(email=post['login_em'])
            if not bcrypt.checkpw(post['login_pw'].encode(), user.password.encode()):
                errors['login_pw'] = "Incorrect email/password combination"
        return errors

class BookManager(models.Manager):
    def book_validator(self, post):
        errors = {}
        if len(post['title']) < 1:
            errors['title'] = "Book must have a title"
        if len(post['description']) < 5:
            errors['description'] = "Description must be at least 5 characters"

        return errors

#Models
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    added_user = models.ForeignKey(User, related_name="books_added", on_delete = models.CASCADE)
    favorite_users = models.ManyToManyField(User, related_name="favorite_books")
    objects = BookManager()