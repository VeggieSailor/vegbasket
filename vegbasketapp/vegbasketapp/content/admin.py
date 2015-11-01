from django.contrib import admin
# Register your models here.
from vegbasketapp.content.models import VeggieSailorRegion, VeggieSailorCousine, VeggieSailorEntry 

class VSEntryAdmin(admin.ModelAdmin):
    pass
admin.site.register(VeggieSailorEntry, VSEntryAdmin)

class VSRegionAdmin(admin.ModelAdmin):
    pass
admin.site.register(VeggieSailorRegion, VSRegionAdmin)

class VSCousineAdmin(admin.ModelAdmin):
    pass
admin.site.register(VeggieSailorCousine, VSCousineAdmin)

