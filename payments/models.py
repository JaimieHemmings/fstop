from django.db import models
from django_countries.fields import CountryField
import uuid
from ckeditor.fields import RichTextField


class Payment(models.Model):
    #Generate unique ID for every payment
    def _generate_payment_id(self):
        return uuid.uuid4().hex.upper()

    payment_id = models.CharField(max_length=32, null=False, editable=False, default=_generate_payment_id)

    full_name = models.CharField(max_length=50, null=False, blank=False, default='')
    email = models.EmailField(max_length=254, null=False, blank=False, default='')
    phone_number = models.CharField(max_length=20, null=False, blank=False, default='')
    date = models.DateTimeField(auto_now_add=True)

    street_address1 = models.CharField(max_length=80, null=False, blank=False, default='')
    street_address2 = models.CharField(max_length=80, null=True, blank=True, default='')
    town_or_city = models.CharField(max_length=40, null=False, blank=False, default='')
    county = models.CharField(max_length=80, null=True, blank=True, default='')
    country = CountryField(blank_label='Country *', null=False, blank=False, default='')
    postcode = models.CharField(max_length=20, null=True, blank=True)
    
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    paid_date = models.DateTimeField(null=True, blank=True)
    stripe_id = models.CharField(max_length=255, blank=True, null=True)
    description = RichTextField(config_name='default')

    def _generate_payment_id(self):
        """
        Generate a random, unique payment id using UUID
        """
        return uuid.uuid4().hex.upper()
    
    def save(self, *args, **kwargs):
        """
        Override the original save method to set the payment id
        if it hasn't been set already.
        """
        if not self.payment_id:
            self.payment_id = self._generate_payment_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email
