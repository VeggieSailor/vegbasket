from django.contrib import admin

from .models import Ingredient, Recipe, IngredientImage, RecipeImage

@admin.register(RecipeImage)
class RecipeImageAdmin(admin.ModelAdmin):
    """Admin class for RecipeImage.
    """
    pass

@admin.register(IngredientImage)
class IngredientImageAdmin(admin.ModelAdmin):
    """Admin class for IngredientImage.
    """
    pass

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Admin class for Recipe.
    """
    pass

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """Admin class for Ingredient.
    """
    pass