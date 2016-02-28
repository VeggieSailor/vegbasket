from django.contrib import admin
# Register your models here.
from vegbasketapp.content.models import VeggieSailorRegion, VeggieSailorCuisine, VeggieSailorEntry

class VSEntryAdmin(admin.ModelAdmin):
    """Admin class for VSEntry.
    """
    pass
admin.site.register(VeggieSailorEntry, VSEntryAdmin)

class VSRegionAdmin(admin.ModelAdmin):
    """Admin class for VSRegion.
    """
    pass
admin.site.register(VeggieSailorRegion, VSRegionAdmin)

class VSCuisineAdmin(admin.ModelAdmin):
    """Admin class for VSCuisine.
    """
    pass
admin.site.register(VeggieSailorCuisine, VSCuisineAdmin)

