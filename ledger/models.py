# ledger/models.py

from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=100, default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:ingredient-detail', args=[str(self.pk)])

class Recipe(models.Model):
    name = models.CharField(max_length=255)

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
