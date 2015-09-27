from django.db import models

class VeggieSailorRegion(models.Model):
    name = models.CharField(max_length=512, default="")
    parent = models.ForeignKey('self', null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)    
    
    
class VeggieSailorEntry(models.Model):
    name = models.CharField(max_length=512, default="")
    summary = models.CharField(max_length=512, default="")
    description = models.TextField(default="")
    region = models.ForeignKey(VeggieSailorRegion, null=False)
    results_geo_place = models.TextField(null=False, blank=True, default="")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

  