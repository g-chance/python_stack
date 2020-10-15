from django.db import models

#MANAGERS
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "Please enter a valid first name"
        if len(postData['first_name']) > 2 and not str.isalpha(postData['first_name']):
            errors['first_name'] = "Your name may not contain numbers"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Please enter a valid last name"
        if len(postData['last_name']) > 2 and not str.isalpha(postData['last_name']):
            errors['last_name'] = "Your name may not contain numbers"
        return errors
    
    def login_validator(self, postData):
        errors = {}

        return errors

#MODELS
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()