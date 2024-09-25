from django.db import models


class Message(models.Model):
    fname = models.CharField(max_length=100, blank=False, null=False)
    lname = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return (
            f"{self.fname} {self.lname} - {self.created_at.strftime('%d/%m/%Y %H:%M')}"
        )
