from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from filebrowser.fields import FileBrowseField


    
class Ingredient(models.Model):
    name = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(max_length=128, unique=True)
    active = models.BooleanField(default=True, null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)    
    description = models.TextField(blank=True, null=False, default="")
    author = models.ForeignKey(User)
    def __str__(self):
        return self.name

 
class IngredientImage(models.Model):
    ingredient = models.ForeignKey(Ingredient)
    description = models.TextField(blank=True, null=False, default="")
    photo = FileBrowseField("Image", max_length=200, directory="recipes/ingimgs/", extensions=[".jpg", ".jpeg", ".png"], null=False)
    def __str__(self):
        return self.photo.name 
 




class Recipe(models.Model):
    name = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(max_length=128, unique=True)
    active = models.BooleanField(default=False, null=False)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)    
    method = models.TextField(blank=True, null=False, default="")
    #ingredients = models.ManyToManyField(IngredientAmount)    
    author = models.ForeignKey(User)
    
    def __str__(self):
        return self.name    
    
class IngredientAmount(models.Model):
    recipe= models.ForeignKey(Recipe)    
    ingredient = models.ForeignKey(Ingredient)
    amount = models.TextField(max_length=256)
    def __str__(self):
        return "%s %s" % (self.ingredient.name, self.amount)
    
class RecipeImage(models.Model):
    recipe= models.ForeignKey(Recipe)
    description = models.TextField(blank=True, null=False, default="")
    photo = FileBrowseField("Image", max_length=200, directory="recipes/imgs/", extensions=[".jpg", ".jpeg", ".png"], null=False)

    def __str__(self):
        return self.photo.name



