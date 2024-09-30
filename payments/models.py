from django.db import models
from django_countries.fields import CountryField


class Payment(models.Model):
    payment_id = models.CharField(max_length=32, null=False, editable=False, default='')
    full_name = models.CharField(max_length=50, null=False, blank=False, default='')
    email = models.EmailField(max_length=254, null=False, blank=False, default='')
    phone_number = models.CharField(max_length=20, null=False, blank=False, default='')
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False, default='')
    street_address1 = models.CharField(max_length=80, null=False, blank=False, default='')
    street_address2 = models.CharField(max_length=80, null=False, blank=False, default='')
    county = models.CharField(max_length=80, null=False, blank=True, default='')
    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    paid_date = models.DateTimeField(null=True, blank=True)
    stripe_id = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.email
