from django.db import models
import json
# Create your models here.

class Region(models.Model):
    parent = models.ForeignKey('self', null=True)
    source_id = models.IntegerField(null=False, unique=True)
    results_source = models.TextField(null=False, blank=True, default="")
    created = models.DateTimeField(auto_now_add=True)
    modified_source = models.DateTimeField(null=True)
    def __str__(self):
        return '%s' % (self.source_id,)

class Entry(models.Model):
    region = models.ForeignKey(Region, null=False)
    source_id = models.IntegerField(null=False, unique=True)
    results_source = models.TextField(null=False, blank=True, default="")
    results_geo = models.TextField(null=False, blank=True, default="")
    results_geo_place = models.TextField(null=False, blank=True, default="")
    created = models.DateTimeField(auto_now_add=True)
    modified_source = models.DateTimeField(null=True)
    modified_geo = models.DateTimeField(null=True)
    obj = None
    obj_geo = None

    def set_obj(self):
        if not self.obj:
            self.obj = json.loads(self.results_source)

    def set_obj_geo(self):
        if not self.obj_geo:
            self.obj_geo = json.loads(self.results_geo)

    def get_address_str(self):
        self.set_obj()
        add1 = self.obj.get('address1', '')
        add2 = self.obj.get('address2', '')
        city = self.obj.get('city', '')
        postal_code = self.obj.get('postal_code', '')
        country = self.obj.get('country', '')
        address = "%s, %s, %s, %s, %s" % (add1, add2, city, postal_code, country)
        return address

    def get_cord(self):
        self.set_obj_geo()
        lng = self.obj_geo['results'][0]['geometry']['location']['lng']
        lat = self.obj_geo['results'][0]['geometry']['location']['lat']

        # print (self.obj_geo['results'][0]['geometry']['location']['place_id']
        # )
        return {'lng': lng, 'lat':lat}
