from django.db import models
import bcrypt
import re

# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "Your first_name must be at least 2 characters"
        if not str.isalpha(postData['first_name']) and len(postData['first_name']) > 0:
            errors['first_name'] = "First name must not contain numbers"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Your last_name must be at least 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Not a valid email address"
        if len(User.objects.filter(email=postData['email'])):
            errors['email'] = "Username not available"
        if postData['password'] != postData['confirm']:
            errors['password'] = "Passwords don't match"
        return errors

    def validate_login(self, postData):
        errors = {}
        if not User.objects.filter(email=postData['email']):
            errors['email'] = "invalid email address"
        else:
            user = User.objects.filter(email=postData['email'])
            if not bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()):
                errors['password'] = "Wrong password"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()