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
	created = models.DateTimeField(auto_now_add=True)
	modified_source = models.DateTimeField(null=True)
	modified_geo = models.DateTimeField(null=True)
	obj = None
	def get_address_str(self):
		if not self.obj:
			self.obj = json.loads(self.results_source)
		obj = self.obj
		add1 = obj.get('address1', '')
		add2 = obj.get('address2', '')
		city = obj.get('city', '')
		postal_code = obj.get('postal_code', '')
		country = obj.get('country', '')
		address = "%s, %s, %s, %s, %s" % (add1, add2, city, postal_code, country)
		return address