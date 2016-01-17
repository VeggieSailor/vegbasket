#import datetime

from django.db import models
import json
from django.utils import timezone

class Region(models.Model):
    """VegGuide region class.
    
    """
    parent = models.ForeignKey('self', null=True)
    source_id = models.IntegerField(null=False, unique=True)
    results_source = models.TextField(null=False, blank=True, default="")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=timezone.now)
    modified_source = models.DateTimeField(null=True)
    obj = None

    def get_children(self):
        """Get children of the region.
        
        """
        self.set_obj()
        if 'children' not in self.obj:
            return []
        result = [ x['uri'].split('/')[-1] for x in self.obj['children'] ]
        return result

    def set_obj(self):
        """Create object from the json string.
        
        """
        if not self.obj:
            self.obj = json.loads(self.results_source)

    def __str__(self):
        self.set_obj()
        try:
            return '%s - %s' % (self.source_id,self.obj['name'])
        except (KeyError,AttributeError) as e:
            return '%s - %s' % (self.source_id,"[[ no name ]]")

class Entry(models.Model):
    """VegGuide entry class.
        
    """    
    region = models.ForeignKey(Region, null=False)
    source_id = models.IntegerField(null=False, unique=True)
    results_source = models.TextField(null=False, blank=True, default="")
    results_geo = models.TextField(null=False, blank=True, default="")
    results_geo_place = models.TextField(null=False, blank=True, default="")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    modified_source = models.DateTimeField(null=True)
    modified_geo = models.DateTimeField(null=True)
    obj = None
    obj_geo = None

    def set_obj(self):
        """Create object from the json string.
        
        """        
        if not self.obj:
            self.obj = json.loads(self.results_source)

    def set_obj_geo(self):
        """Create geo object from the json string.
        
        """        
        if not self.obj_geo:
            self.obj_geo = json.loads(self.results_geo)

    def get_elem(self, elem, default=''):
        """Get elem by name from json obj.
        
        """
        self.set_obj()
        result = self.obj.get(elem, default)
        return result

    def get_credits_string(self):
        """Get credits string for HTML.
        
        """
        name = self.get_elem('user')['name']
        uri = self.get_elem('user')['uri']
        return 'Added by <a target="_blank"  href="%s">%s</a>' % (uri, name)

    def get_address_str(self):
        """Get address.
        
        """
        self.set_obj()
        add1 = self.obj.get('address1', '')
        add2 = self.obj.get('address2', '')
        city = self.obj.get('city', '')
        postal_code = self.obj.get('postal_code', '')
        country = self.obj.get('country', '')
        address = "%s, %s, %s, %s, %s" % (add1, add2, city, postal_code, country)
        return address

    def get_cord(self):
        """Get coordinates.
        
        """
        self.set_obj_geo()
        lng = self.obj_geo['results'][0]['geometry']['location']['lng']
        lat = self.obj_geo['results'][0]['geometry']['location']['lat']
        return {'lng': lng, 'lat':lat}

    def get_name(self):
        """Get the name of the entry.
        
        """
        self.set_obj()
        try:
            name = self.obj['name']
        except TypeError: 
            name = None
        return name
    
    def get_short_description(self):
        """Get the short description.
        
        """
        self.set_obj()
        short_description = self.obj['short_description']        
        return short_description
    
    
    def get_long_description(self):
        """Get the long description.
        
        """
        self.set_obj()
        try:
            long_description = self.obj['long_description'] ['text/html']    
            ##long_description = json.loads(long_description)['text/html']
        except KeyError:
            long_description = ''
            
        return long_description    
    def get_postal_code(self):
        """Get the postal code.
        
        """
        self.set_obj()
        try:
            postal_code = self.obj['postal_code']
        except KeyError:
            postal_code = ''
        return postal_code


    def __str__(self):
        self.set_obj()
        name = self.obj.get('name', 'Unknown name')
        city = self.obj.get('city', 'Unknown city')
        return '%s - %s, %s' % (self.source_id,name, city)

    class Meta:
        verbose_name_plural = "entries"

class Reviews(models.Model):
    """Reviews transformer model.

    Attributes
    ----------

    entry : Entry, foreign key 
    source_id : int, id of the entry
    results_source : str, result of the origin VegGuide.org call
    created : datetime, timestamp of the creation
    modified_source : datetime, timestamp of the last modification
    """
    entry = models.OneToOneField(Entry, null=False)
    source_id = models.IntegerField(null=False, unique=True)
    results_source = models.TextField(null=False, blank=True, default="")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)    
    modified_source = models.DateTimeField(null=True)
    obj = None

    def set_obj(self):
        """Create object from the json string.
        """        
        if not self.obj:
            self.obj = json.loads(self.results_source)

    def __str__(self):
        self.set_obj()
        return '%s' % (self.entry.__str__())
    
    class Meta:
        verbose_name_plural = "reviews"
