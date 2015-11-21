from django.db import models

from vegbasketapp.transformer.models import Region
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class VeggieSailorCategory(models.Model):
    """Main Veggie Sailor Category.
    
    """
    name = models.CharField(max_length=128)

    def __str__(self):
        return "%s" % self.name       

class VeggieSailorCuisine(models.Model):
    """Main Veggie Sailor Cuisine.
    
    """    
    name = models.CharField(max_length=128, default="")
    parent = models.ForeignKey('self', null=True)
    description = models.TextField(default="")

    def __str__(self):
        return "%s" % self.name       

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

    def get_parents_list(self, elems=None):
        """Get names of the parents in a recursive way.
                
        """        
        if elems is None:
            elems = []
        
        elems.append(self.name)
        if self.parent:
            elems = self.parent.get_parents_list(elems)
        return elems
    
    def __str__(self):
        return "%s" % self.name    

class VeggieSailorEntry(models.Model):
    """Main Veggie Sailor Entry.
    """    
    name = models.CharField(max_length=512, default="")
    short_description = models.CharField(max_length=512, default="")
    description = models.TextField(default="")
    address1 = models.CharField(max_length=256, default="")
    address2 = models.CharField(max_length=256, default="")
    city = models.CharField(max_length=256, default="")
    zipcode = models.CharField(max_length=32, default="")
    summary = models.CharField(max_length=512, default="")
    
    region = models.ForeignKey(VeggieSailorRegion, null=False)
    
    results_geo_place = models.TextField(null=False, blank=True, default="")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id') 
    
    vg_object_id = models.IntegerField(null=True)
    
    categories = models.ManyToManyField(VeggieSailorCategory)
    cuisines = models.ManyToManyField(VeggieSailorCuisine)
    
    
    def __unicode__(self):
        return u"%s" % self.name    
    def __str__(self):
        return "%s in %s" % (self.name, self.region.name)
    
    def get_images_height(self, height):
        return self.veggiesailorimage_set.filter(height='%s' % height)
    
    def get_images_height_400(self):
        return self.get_images_height(400)
       
    class Meta:
        verbose_name_plural = "veggie sailor entries"

class VeggieSailorImage(models.Model):
    """Class storing images for the entries.
    
    """
    title = models.CharField(max_length=256, default="")
    entry = models.ForeignKey(VeggieSailorEntry, null=False)
    photo = models.ImageField(upload_to='entries/photos',
                              height_field='height',
                              width_field='width')
    height = models.IntegerField()
    width = models.IntegerField()
    







