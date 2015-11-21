from django.contrib import admin
# Register your models here.
from vegbasketapp.content.models import VeggieSailorRegion, VeggieSailorCuisine, VeggieSailorEntry 

class VSEntryAdmin(admin.ModelAdmin):
    pass
admin.site.register(VeggieSailorEntry, VSEntryAdmin)

class VSRegionAdmin(admin.ModelAdmin):
    pass
admin.site.register(VeggieSailorRegion, VSRegionAdmin)

class VSCuisineAdmin(admin.ModelAdmin):
    pass
admin.site.register(VeggieSailorCuisine, VSCuisineAdmin)

