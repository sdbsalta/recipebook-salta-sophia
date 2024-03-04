# ledger/views.py
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        "recipes": [recipe.name for recipe in recipes],
    }
    return render(request, 'recipe_list.html', ctx)

def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ctx = {
        "recipe": recipe,
        }
    return render(request, 'recipe_detail.html', ctx)

class RecipeListView(ListView):
    model = Recipe
    template_name = "recipe_list.html"
    
class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipe_detail.html"
