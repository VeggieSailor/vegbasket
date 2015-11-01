from django.db import models

from vegbasketapp.transformer.models import Region

class VeggieSailorRegion(models.Model):
    """Main Veggie Sailor Region.
    """
    name = models.CharField(max_length=512, default="")    
    parent = models.ForeignKey('self', null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    source_region = models.ForeignKey(Region, null=True, unique=True)

class VeggieSailorEntry(models.Model):
    """Main Veggie Sailor Entry.
    """    
    name = models.CharField(max_length=512, default="")
    short_description = models.CharField(max_length=512, default="")
    description = models.TextField(default="")    
    summary = models.CharField(max_length=512, default="")
    region = models.ForeignKey(VeggieSailorRegion, null=False)
    results_geo_place = models.TextField(null=False, blank=True, default="")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = "veggie sailor entries"

class VeggieSailorCousine(models.Model):
    """Main Veggie Sailor Cousine.
    """    
    name = models.CharField(max_length=128, default="")
    parent = models.ForeignKey('self', null=True)
    description = models.TextField(default="")
