from django.db import models

# Create your models here.
class Wizard(models.Model):
    name = models.CharField(max_length=45)
    house = models.CharField(max_length=45)
    pet = models.CharField(max_length=45)
    year = models.IntegerField()

    def __repr__(self):
        return f"Movie object: name: {self.name}, house: {self.house}, pet: {self.pet}, year: {self.year}"