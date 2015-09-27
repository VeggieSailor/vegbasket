from django.db import models

# Create your models here.

from django.db import models
import json


class VeggieSailorRegion(models.Model):
    name = models.CharField(max_length=512, default="")
    parent = models.ForeignKey('self', null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)    
    
    
class VeggieSailorEntry(models.Model):
    name = models.CharField(max_length=512, default="")
    summary = models.CharField(max_length=512, default="")
    description = models.TextField(default="")
    region = models.ForeignKey(Region, null=False)
    results_geo_place = models.TextField(null=False, blank=True, default="")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

  