from django.contrib import admin
# Register your models here.
from vegbasketapp.transformer.models import Entry, Region

class EntryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Entry, EntryAdmin)

class RegionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Region, RegionAdmin)