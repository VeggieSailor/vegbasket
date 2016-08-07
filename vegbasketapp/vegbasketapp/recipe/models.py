from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from vegbasketapp.content.models import VeggieSailorEntry
# Create your models here.

from filebrowser.fields import FileBrowseField

from django.core.urlresolvers import reverse
    
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
    class Meta:
        ordering = ['-modified']

 
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
    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'slug': self.slug})
    
    def __str__(self):
        return self.name    
    

class RecipeTime(models.Model):
    recipe= models.ForeignKey(Recipe)    
    
    time = models.IntegerField(null=False, default=10)
    step = models.TextField(max_length=128, blank=False, null=False)
    def __str__(self):
        return "%sm %s" % (self.time, self.step )
    
    
class IngredientAmount(models.Model):
    recipe= models.ForeignKey(Recipe)    
    ingredient = models.ForeignKey(Ingredient)
    amount = models.TextField(max_length=256)
    def __str__(self):
        return "%s %s" % (self.ingredient.name, self.amount)
    class Meta:
        ordering = ['-ingredient']    
    
class RecipeImage(models.Model):
    recipe= models.ForeignKey(Recipe)
    description = models.TextField(blank=True, null=False, default="")
    photo = FileBrowseField("Image", max_length=200, directory="recipes/imgs/", extensions=[".jpg", ".jpeg", ".png"], null=False)

    def __str__(self):
        return self.photo.name





#class Visit(models.Model):
    #"""Logs the visit in the place.
    #"""
    #user = models.ForeignKey(User)
    #note = models.TextField(default='', null=False)
    #created = models.DateTimeField(auto_now_add=True)
    #modified = models.DateTimeField(auto_now=timezone.now)
    #visit_timestamp = models.DateTimeField(null=False)
    #entry = models.ForeignKey(VeggieSailorEntry)
    #rating = models.IntegerField(null=True)
    
    #def __str__(self):
        #return '%s at %s on %s' % (self.user.username, self.entry.name, self.visit_timestamp)




class CookEntry(models.Model):
    """Logs the cooking of the recipe.
    """
    user = models.ForeignKey(User)
    note = models.TextField(default='', null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=timezone.now)
    visit_timestamp = models.DateTimeField(null=False)
    recipe = models.ForeignKey(Recipe)
    rating = models.IntegerField(null=True)
    
    def __str__(self):
        return '%s at %s on %s' % (self.user.username, self.entry.name, self.visit_timestamp)
