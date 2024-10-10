from django.db import models
import uuid

class ServicesPage(models.Model):
    """
    A model to define the services page
    """
    def get_path(instance, filename):
        extension = filename.split(".")[-1]
        filename = f"{filename}-{uuid.uuid4()}.{extension}"
        return f"services/{filename}"
    
    title = models.CharField(max_length=100)

    hero_title = models.CharField(max_length=100)
    hero_image = models.ImageField(upload_to=get_path, null=False, blank=False)

    banner_image = models.ImageField(upload_to=get_path, null=False, blank=False)
    banner_alt_text = models.CharField(max_length=100)

    highlight_one_title = models.CharField(max_length=100)
    highlight_one_lead = models.CharField(max_length=500)
    highlight_one_image = models.ImageField(upload_to=get_path, null=False, blank=False)
    highlight_one_alt_text = models.CharField(max_length=100)

    highlight_two_title = models.CharField(max_length=100)
    highlight_two_lead = models.CharField(max_length=500)
    highlight_two_image = models.ImageField(upload_to=get_path, null=False, blank=False)
    highlight_two_alt_text = models.CharField(max_length=100)

    service_info_one_title = models.CharField(max_length=100)
    service_info_one_lead = models.TextField()
    service_info_one_image = models.ImageField(upload_to=get_path, null=False, blank=False)
    service_info_one_alt_text = models.CharField(max_length=100)

    service_info_two_title = models.CharField(max_length=100)
    service_info_two_lead = models.TextField()
    service_info_two_image = models.ImageField(upload_to=get_path, null=False, blank=False)
    service_info_two_alt_text = models.CharField(max_length=100)
    

    def __str__(self):
        return self.title