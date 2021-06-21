from django.conf import settings
from django.contrib.auth import get_user_model
from .models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.models import Group

User = get_user_model()

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='Customer')
        instance.groups.add(group)
        Profile.objects.create(user=instance)
        print('Profile Created')

# post_save.connect(create_profile,sender=User)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()