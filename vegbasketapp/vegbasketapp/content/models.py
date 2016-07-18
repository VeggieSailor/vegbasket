from django.utils.translation import ugettext_lazy as _
from django.contrib.gis.geos import Point

import datetime as dt

from django.db import models
from django.utils import timezone

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from vegbasketapp.transformer.models import Region

from autoslug import AutoSlugField
VEG_LEVEL_CHOICES = (
    (0, _('Not Veg-Friendly')),
    (1, _('Vegetarian-Friendly')),
    (2, _('Vegan-Friendly')),
    (3, _('Vegetarian (But Not Vegan-Friendly)')),
    (4, _('Vegetarian')),
    (5, _('Vegan')),
    
)


# From Katya
# F44336    0 - Not Veg-Friendly
# 2764AE    1 - Vegetarian-Friendly
# 388E3C    2 - Vegan-Friendly
# F38F1B    3 - Vegetarian (But Not Vegan-Friendly)
# 60C4E3    4 - Vegetarian
# 88BD24    5 - Vegan

PRICE_CHOICES = (
    (0, _('Unknown')),
    (1, _('Inexpensive')),
    (2, _('Average')),
    (3, _('Expensive')),   
)

SMOKING_STATUS = ['Not clear', 'Yes', 'No', 'Not sure']

SMOKING_STATUS_TRANS = _(' '.join(SMOKING_STATUS)) 
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
    class Meta:
        app_label = "content"

class VeggieSailorRegion(models.Model):
    """Main Veggie Sailor Region.
    """
    name = models.CharField(max_length=512, default="")    
    parent = models.ForeignKey('self', null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    source_region = models.OneToOneField(Region, null=True)
    
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
    class Meta:
        app_label = "content"
    

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
    # Coordinates
    long = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    

    def get_rating_lists(self):
        """Get the rankings for the display.
        """
        full = int(self.rating)
        half = 1 if self.rating-int(self.rating)>0 else 0
        empty = 5 - half - full
        return (range(full), range(half), range(empty))

    def get_opening_hours_display(self):
        """Get opening hours in the human format.
        """
        hours = self.opening_hours.all()

        results = []

        for hour in hours:
            if hour.is_closed is True:
                results.append((
                    hour.get_weekday_display(),
                    _("closed")
                ))                
            else:
                results.append((
                    hour.get_weekday_display(),
                    hour.from_hour,
                    hour.to_hour()
                ))
        return results

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

        if value is None:
            return SMOKING_STATUS[0]
        elif self.allows_smoking == '0':
            return SMOKING_STATUS[1]
        elif self.allows_smoking == '1':
            return SMOKING_STATUS[2]
        return SMOKING_STATUS[3] # huh?

    def allows_smoking_verbose(self):
        """Get smoking verbose info.
        """
        return self.get_boolean_verbose("allows_smoking")

    def allows_reservations_verbose(self):
        """Get reservations verbose info.
        """
        return self.get_boolean_verbose("allows_reservations")

    def is_open(self):
        """If the place is open right now.
        """
        result = True if True in [x.is_open() for x in self.opening_hours.all() ] else False
        return result
    
    def is_open_verbose(self):
        """Check if it is open now.
        """
        msg_closed = _('Closed now')
        msg_open = _('Open now')
        if self.is_open() is True:
            return '( <span class="green">%s</span> )' % msg_open
        else:
            return '( <span class="vs-alert">%s</span> )' % msg_closed
    def get_absolute_url(self):
        return reverse('vegbasketapp.frontend.views.entry_slug', args=[str(self.slug)])
        #return reverse('vegbasketapp.frontend.views.entry_vs', args=[str(self.id)])
       
    class Meta:
        """Meta class for the model.
        """
        verbose_name_plural = "veggie sailor entries"
        app_label = "content"
        
    def get_location(self):
        """Get the location - for the Haystack.
        """
        print (self.long, self.lat)
        if not self.long or not self.lat:
            return Point(0,0)    
        return Point(float(self.long), float(self.lat))    

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
    entry = models.ForeignKey(VeggieSailorEntry, related_name='opening_hours')
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
    
    def to_hour(self):
        """Get closing hour.
        http://stackoverflow.com/questions/12448592/how-to-add-delta-to-python-datetime-time
        """

        delta = self.duration
        t = self.from_hour       
        result = (dt.datetime.combine(dt.date(1,1,1),t) + delta).time()
        return result

    def is_open(self):
        """If the place is open right now.
        """
        current_day = dt.date.weekday(dt.date.today())
        current_time = dt.datetime.now().time()
        if current_day == self.weekday:
            if current_time <= self.from_hour and current_time <= self.to_hour():
                return True
        return False



    def __unicode__(self):
        return u"%s - %s - %s %s" % (self.entry.id, self.entry.name,
                                     self.get_weekday_display(), self.from_hour)
    def __str__(self):
        return u"%s - %s - %s %s" % (self.entry.id, self.entry.name,
                                     self.get_weekday_display(), self.from_hour)

    class Meta:
        unique_together = (("entry", "from_hour", "weekday", "is_closed"),)
        ordering = ['weekday', 'from_hour']

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

class VeggieSailorRating(models.Model):
    """Rates the place.
    """
    user = models.ForeignKey(User)
    note = models.TextField(default='', null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=timezone.now)
    entry = models.ForeignKey(VeggieSailorEntry)
    rating = models.IntegerField(null=False)

