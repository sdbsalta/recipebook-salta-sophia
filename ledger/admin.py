from django.contrib import admin

from .models import Recipe, RecipeIngredient

class RecipeIngredientInline(admin.TabularInline):  
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline]

admin.site.register(Recipe, RecipeAdmin)