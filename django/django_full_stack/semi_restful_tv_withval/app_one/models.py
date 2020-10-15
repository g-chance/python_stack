from django.db import models
from datetime import date, datetime

# Create your models here.

class ShowManager(models.Manager):
    def basic_validator(self, postData, title=None):
        errors = {}

        if len(postData['title']) < 2:
            errors['title'] = "Your title must be at least 2 characters"
        if len(postData['network']) < 3:
            errors['network'] = "Your network must be at least 3 characters"
        if len(postData['description']) < 10 and len(postData['description']) > 0:
            errors['description'] = "Your description must be at least 10 characters"
        release_date = datetime.strptime(postData['release_date'],"%Y-%m-%d")
        if release_date > datetime.today():
            errors['release_date'] = "Your date is TOOOOO LARGEEE"
        if title != None:
            if len(Show.objects.filter(title=postData['title'])) > 0:
                if Show.objects.get(title=postData['title']).title != title:
                    errors['title'] = "Your title must be unique"
        elif len(Show.objects.filter(title=postData['title'])) > 0:
            errors['title'] = "Your title must be unique"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()