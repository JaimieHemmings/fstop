from django.db import models
import uuid

class ServicesHero(models.Model):
    """
    A model to define the services hero image
    """
    def get_path(instance, filename):
        extension = filename.split(".")[-1]
        filename = f"{filename}-{uuid.uuid4()}.{extension}"
        return f"services/hero/{filename}"
    
    title = models.CharField(max_length=100)
    lead = models.CharField(max_length=500)
    image = models.ImageField(upload_to=get_path)
    alt_text = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class ServicesBanner(models.Model):
    """
    A model to define the services banner image
    """
    def get_path(instance, filename):
        extension = filename.split(".")[-1]
        filename = f"{filename}-{uuid.uuid4()}.{extension}"
        return f"services/banner/{filename}"
    
    image = models.ImageField(upload_to=get_path)
    alt_text = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class ServicesCards(models.Model):
    """
    A model to define the services cards
    """    
    title = models.CharField(max_length=100)
    lead = models.CharField(max_length=500)
    icon = models.CharField(max_length=2000)

    def __str__(self):
        return self.title
    

class ServicesContextBannerOne(models.Model):
    """
    A model to define the services context banner one
    """
    def get_path(instance, filename):
        extension = filename.split(".")[-1]
        filename = f"{filename}-{uuid.uuid4()}.{extension}"
        return f"services/context/banner_one/{filename}"
    
    title = models.CharField(max_length=100)
    lead = models.CharField(max_length=500)
    image = models.ImageField(upload_to=get_path)
    alt_text = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class ServicesContextBannerTwo(models.Model):
  """
  A model to define the services context banner two
  """
  def get_path(instance, filename):
      extension = filename.split(".")[-1]
      filename = f"{filename}-{uuid.uuid4()}.{extension}"
      return f"services/context/banner_two/{filename}"

  title = models.CharField(max_length=100)
  lead = models.CharField(max_length=500)
  image = models.ImageField(upload_to=get_path)
  alt_text = models.CharField(max_length=100)

  def __str__(self):
      return self.title
