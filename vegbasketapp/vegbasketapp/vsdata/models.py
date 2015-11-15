from django.db import models

from vegbasketapp.transformer.models import Region
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class VeggieSailorRegion(models.Model):
    """Main Veggie Sailor Region.
    """
    name = models.CharField(max_length=512, default="")    
    parent = models.ForeignKey('self', null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    source_region = models.ForeignKey(Region, null=True, unique=True)
    
    content_type = models.ForeignKey(ContentType, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return "%s " % self.name    

class VeggieSailorEntry(models.Model):
    """Main Veggie Sailor Entry.
    """    
    name = models.CharField(max_length=512, default="")
    short_description = models.CharField(max_length=512, default="")
    description = models.TextField(default="")
    address1 = models.CharField(max_length=256, default="")
    address2 = models.CharField(max_length=256, default="")
    zipcode = models.CharField(max_length=32, default="")
    summary = models.CharField(max_length=512, default="")
    region = models.ForeignKey(VeggieSailorRegion, null=False)
    results_geo_place = models.TextField(null=False, blank=True, default="")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id') 
    
    def __unicode__(self):
        return u"%s" % self.name    
    def __str__(self):
        return "%s in %s" % (self.name, self.region.name)
    
    class Meta:
        verbose_name_plural = "veggie sailor entries"

class VeggieSailorCousine(models.Model):
    """Main Veggie Sailor Cousine.
    """    
    name = models.CharField(max_length=128, default="")
    parent = models.ForeignKey('self', null=True)
    description = models.TextField(default="")


    