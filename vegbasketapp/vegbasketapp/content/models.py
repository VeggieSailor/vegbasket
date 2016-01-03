from django.db import models
from django.utils.translation import ugettext as _
from vegbasketapp.transformer.models import Region
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from django.core.urlresolvers import reverse
from autoslug import AutoSlugField
VEG_LEVEL_CHOICES = (
    (0, 'Not Veg-Friendly'),
    (1, 'Vegetarian-Friendly'),
    (2, 'Vegan-Friendly'),
    (3, 'Vegetarian (But Not Vegan-Friendly)'),
    (4, 'Vegetarian'),
    (5, 'Vegan'),
    
)


# From Katya
# F44336    0 - Not Veg-Friendly
# 2764AE    1 - Vegetarian-Friendly
# 388E3C    2 - Vegan-Friendly
# F38F1B    3 - Vegetarian (But Not Vegan-Friendly)
# 60C4E3    4 - Vegetarian
# 88BD24    5 - Vegan

PRICE_CHOICES = (
    (0,'Unknown'),
    (1, 'Inexpensive'),
    (2, 'Average'),
    (3, 'Expensive'),   
)



class VeggieSailorCategory(models.Model):
    """Main Veggie Sailor Category.
    
    """
    name = models.CharField(max_length=128)

    def __str__(self):
        return "%s" % self.name       

class VeggieSailorPayment(models.Model):
    """Main Veggie Sailor Payment.
    
    """
    name = models.CharField(max_length=128)

    def __str__(self):
        return "%s" % self.name    

class VeggieSailorTag(models.Model):
    """Main Veggie Sailor Tag.
    
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
    slug = models.SlugField()
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
    
    allows_smoking = models.NullBooleanField(null=True)
    allows_reservations = models.NullBooleanField(null=True)
    categories = models.ManyToManyField(VeggieSailorCategory)
    cuisines = models.ManyToManyField(VeggieSailorCuisine)
    tags = models.ManyToManyField(VeggieSailorTag)
    payments = models.ManyToManyField(VeggieSailorPayment)
    
    level = models.IntegerField(choices = VEG_LEVEL_CHOICES,default=0)
    price = models.IntegerField(choices = PRICE_CHOICES,default=0)
    
    rating = models.FloatField(default="0.0", null=False)
    rating_count = models.IntegerField(default=0, null=False)
    

    def get_rating_lists(self):
        full = int(self.rating)
        half = 1 if self.rating-int(self.rating)>0 else 0
        empty = 5 - half - full
        return (range(full), range(half), range(empty))
        
        
    
    
    def __unicode__(self):
        return u"%s" % self.name    
    def __str__(self):
        return "%s in %s" % (self.name, self.region.name)
    
    def get_images_height(self, height):
        return self.veggiesailorimage_set.filter(height='%s' % height)
    
    def get_images_width_height(self, width, height):
        return self.veggiesailorimage_set.filter(width='%s' % width, height='%s' % height)
            
    
    def get_images_600_400(self)    :
        return self.get_images_width_height(600, 400)

    def get_images_533_400(self)    :
        return self.get_images_width_height(533, 400)
    
    def get_images_height_400(self):
        return self.get_images_height(400)


    def get_images_height_348(self):
        return self.get_images_height(348)

    def get_boolean_verbose(self, field):
        
        value = self.__getattribute__(field)
        #print (field,value)
        
        
        if value is None:
            return "Not clear"
        elif self.allows_smoking == '0':
            return "Yes"
        elif self.allows_smoking == '1':
            return "No"    
        return "Not sure" # huh?

    
    def allows_smoking_verbose(self):
        return self.get_boolean_verbose("allows_smoking")

    def allows_reservations_verbose(self):
        return self.get_boolean_verbose("allows_reservations")


    def get_absolute_url(self):
        return reverse('vegbasketapp.frontend.views.entry_slug', args=[str(self.slug)])
        #return reverse('vegbasketapp.frontend.views.entry_vs', args=[str(self.id)])            
       
    class Meta:
        verbose_name_plural = "veggie sailor entries"

# Inspired (read stolen and rewritten ;) by:
# http://stackoverflow.com/questions/12216771/django-objects-for-business-hours
# http://stackoverflow.com/questions/8128143/any-existing-solution-to-implement-opening-hours-in-django

WEEKDAYS = [
    (0, _("Monday")),
    (1, _("Tuesday")),
    (2, _("Wednesday")),
    (3, _("Thursday")),
    (4, _("Friday")),
    (5, _("Saturday")),
    (6, _("Sunday")),
]

class VeggieSailorOpeningHour(models.Model):
    """Opening hours for the Entry.
    """
    entry = models.ForeignKey(VeggieSailorEntry)
    from_hour = models.TimeField(null=True)
    duration = models.DurationField(null=True)
    weekday = models.IntegerField(
        choices=WEEKDAYS
    )    
    created = models.DateTimeField(
        auto_now_add=True
    )
    modified = models.DateTimeField(
        auto_now=True
    )
    is_closed = models.BooleanField(null=False, default=False)
    class Meta:
        unique_together = (("entry", "from_hour", "weekday", "is_closed"),)

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
    









