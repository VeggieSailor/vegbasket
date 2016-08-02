from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Ingredient(models.Model):
    slug = models.SlugField(max_length=128)
    active = models.BooleanField(default=True, null=False)
    name = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)    
    description = models.TextField(blank=True, null=False, default="")
    author = models.ForeignKey(User)

class IngredientImage(models.Model):
    description = models.TextField(blank=True, null=False, default="")
    photo = models.ImageField(verbose_name=None, name=None, 
                              width_field="width", 
                             height_field="height")
    width = models.IntegerField()
    height = models.IntegerField()
    author = models.ForeignKey(User)

class IngredientAmount(models.Model):
    ingredient = models.ForeignKey(Ingredient)
    amount = models.TextField(max_length=256)

class Recipe(models.Model):
    slug = models.SlugField(max_length=128)
    active = models.BooleanField(default=False, null=False)
    name = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)    
    description = models.TextField(blank=True, null=False, default="")
    ingredients = models.ManyToManyField(Ingredient)    
    author = models.ForeignKey(User)

class RecipeImage(models.Model):
    description = models.TextField(blank=True, null=False, default="")
    photo = models.ImageField(verbose_name=None, name=None, 
                              width_field="width", 
                             height_field="height")
    width = models.IntegerField()
    height = models.IntegerField()
    author = models.ForeignKey(User)

