from django.contrib import admin
from vegbasketapp.diary.models import Visit

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'entry')    
    pass