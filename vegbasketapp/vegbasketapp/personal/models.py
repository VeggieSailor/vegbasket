from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    """Basic user profile model.
    """
    user = models.OneToOneField(User)
    accepted_tos = models.BooleanField(default=False)
    first_time = models.BooleanField(default=True)
    avatar =  models.ImageField(upload_to="img/avatars/")
    class Meta:
        app_label = 'personal'


def create_user_profile(sender, instance, created, **kwargs):
    """Create user profile signal.
    """
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)