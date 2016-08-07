from django.contrib import admin

from .models import Ingredient, Recipe, IngredientImage,\
     RecipeImage, IngredientAmount, RecipeTime


#@admin.register(RecipeImage)
class RecipeImageInline(admin.TabularInline):
    """Admin class for RecipeImage.
    """
    model = RecipeImage
    extra = 2
    max_num = 5


class RecipeTimeInline(admin.TabularInline):
    """Inline for RecipeTime.
    """
    model = RecipeTime
    extra = 2
    max_num = 16


class IngredientImageAdmin(admin.TabularInline):
    """Admin class for IngredientImage.
    """
    model = IngredientImage
    extra = 0    
    max_num = 5
    


class IngredientAmountAdmin(admin.TabularInline):
    """Admin class for IngredientAmount.
    """
    model = IngredientAmount
    extra = 1    
    max_num = 60



    



@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Admin class for Recipe.
    """
    inlines = [
        IngredientAmountAdmin,
        RecipeTimeInline,
        RecipeImageInline,
        
    ]

    def get_form(self, request, obj=None, **kwargs):
        """Prefill forms with the current user.
        """        
        if request.user.is_superuser:        
            form = super(RecipeAdmin, self).get_form(request, obj, **kwargs)
            form.base_fields['author'].initial = request.user
            return form



@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """Admin class for Ingredient.
    """
    inlines = [
        IngredientImageAdmin,
    ]    
    def get_form(self, request, obj=None, **kwargs):
        """Prefill forms with the current user.
        """
        if request.user.is_superuser:        
            form = super(IngredientAdmin, self).get_form(request, obj, **kwargs)
            form.base_fields['author'].initial = request.user
            return form

    def get_ordering(self, request):
        """Thanks for this we are getting correct sorting in admin panel.
        """
        return ['name']
