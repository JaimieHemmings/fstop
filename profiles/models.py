from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=50, blank=True, null=True)
    lname = models.CharField(max_length=50, blank=True, null=True)
    street_address1 = models.CharField(max_length=80, blank=True, null=True)
    street_address2 = models.CharField(max_length=80, blank=True, null=True)
    town_or_city = models.CharField(max_length=40, blank=True, null=True)
    county = models.CharField(max_length=80, blank=True, null=True)
    postcode = models.CharField(max_length=20, blank=True, null=True)
    country = CountryField(blank_label="(Select Country)", null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
