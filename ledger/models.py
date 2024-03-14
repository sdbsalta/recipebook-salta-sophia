# ledger/models.py

from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from django.utils import timezone


class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:ingredient-detail', args=[str(self.pk)])

class Recipe(models.Model):
    name = models.CharField(max_length=255, default='')
    author = models.CharField(max_length=100, null=True)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:recipe-detail', args=[str(self.pk)])

class RecipeIngredient(models.Model):
    quantity = models.FloatField()
    ingredient = models.ForeignKey(
        'Ingredient', 
        on_delete=models.CASCADE, 
        related_name='recipe'
    )
    recipe = models.ForeignKey(
        'Recipe', 
        on_delete=models.CASCADE, 
        related_name='ingredients'
    )
    
    class Meta:
        unique_together = ('ingredient', 'recipe')
        
    def get_absolute_url(self):
        return reverse('ledger:recipe-detail', args=[str(self.pk)])

    def __str__(self):
        return f'{self.quantity} {self.ingredient} in {self.recipe}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    short_bio = models.TextField(
        validators=[
            MinLengthValidator(255, "Bio must be at least 255 characters long.")
        ]
    )
