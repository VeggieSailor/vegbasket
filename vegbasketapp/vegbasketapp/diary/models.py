from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from vegbasketapp.content.models import VeggieSailorEntry

class Visit(models.Model):
    """Logs the visit in the place.
    """
    user = models.ForeignKey(User)
    note = models.TextField(default='', null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=timezone.now)
    visit_timestamp = models.DateField(null=False)
    entry = models.ForeignKey(VeggieSailorEntry)
    rating = models.IntegerField(null=False)
