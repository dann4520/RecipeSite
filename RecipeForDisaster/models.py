from django.db import models
from django.utils import timezone
# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=200, default="Coffee")
    directions = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.directions

class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=20)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.name


