from django.db import models

# Create your models here.

class Recette(models.Model):
    titre = models.CharField(max_length=45)
    ingredients = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    date_creation = models.DateField()
    auteur = models.CharField(max_length=20)

    def __str__(self):
        return self.titre+self.ingredients+self.description+self.date_creation+self.auteur