from django.db import models

class Payment(models.Model):
    user_profile = models.ForeignKey(
        'profiles.UserProfile',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='payments')
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    paid_date = models.DateTimeField(null=True, blank=True)
    stripe_id = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.email