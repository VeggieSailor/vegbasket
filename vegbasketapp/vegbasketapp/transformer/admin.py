from django.contrib import admin
# Register your models here.
from vegbasketapp.transformer.models import Entry, Region, Reviews
from vegbasketapp.transformer.tools_entry import get_entry_by_id
from vegbasketapp.transformer.tools_entry import get_region_by_id



def refresh_entry(modeladmin, request, queryset):
    for i in queryset.all():
        get_entry_by_id(i.source_id, force=True)
refresh_entry.short_description = "Refresh selected sources"

def refresh_region(modeladmin, request, queryset):
    for i in queryset.all():
        get_region_by_id(i.source_id, force=True)
refresh_region.short_description = "Refresh selected sources"


class EntryAdmin(admin.ModelAdmin):
    actions = [refresh_entry]
admin.site.register(Entry, EntryAdmin)

class RegionAdmin(admin.ModelAdmin):
    actions = [refresh_region]
admin.site.register(Region, RegionAdmin)

class ReviewsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Reviews, ReviewsAdmin)