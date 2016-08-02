from django.contrib import admin

from .models import Ingredient, Recipe, IngredientImage, RecipeImage, IngredientAmount
@admin.register(RecipeImage)
class RecipeImageAdmin(admin.ModelAdmin):
    """Admin class for RecipeImage.
    """
    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:        
            form = super(RecipeImageAdmin, self).get_form(request, obj, **kwargs)
            form.base_fields['author'].initial = request.user
            return form

@admin.register(IngredientImage)
class IngredientImageAdmin(admin.ModelAdmin):
    """Admin class for IngredientImage.
    """
    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:        
            form = super(IngredientImageAdmin, self).get_form(request, obj, **kwargs)
            form.base_fields['author'].initial = request.user
            return form
    class Media:
        js = ['/static/admin/js/jquery.min.js','/static/admin/js/jquery.init.js']

@admin.register(IngredientAmount)
class IngredientAmountAdmin(admin.ModelAdmin):
    """Admin class for IngredientAmount.
    """
    pass

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Admin class for Recipe.
    """
    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:        
            form = super(RecipeAdmin, self).get_form(request, obj, **kwargs)
            form.base_fields['author'].initial = request.user
            return form

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """Admin class for Ingredient.
    """
    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:        
            form = super(IngredientAdmin, self).get_form(request, obj, **kwargs)
            form.base_fields['author'].initial = request.user
            return form
