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
    
    
class HomePageHero(models.Model):
    hero_title = models.CharField(max_length=50, blank=False, null=False)
    hero_subtitle = models.TextField(max_length=200, blank=False, null=False)
    hero_image = models.ImageField(upload_to="cms/home/")
    hero_list_one = models.CharField(max_length=100, blank=False, null=False)
    hero_list_two = models.CharField(max_length=100, blank=False, null=False)
    hero_list_three = models.CharField(max_length=100, blank=False, null=False)
    hero_list_four = models.CharField(max_length=100, blank=False, null=False)
    data_one_value = models.IntegerField()
    data_one_title = models.CharField(max_length=50, blank=False, null=False)
    data_two_value = models.IntegerField()
    data_two_title = models.CharField(max_length=50, blank=False, null=False)
    data_three_value = models.IntegerField()
    data_three_title = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return f"{self.hero_title} - {self.hero_subtitle}"
    

class HomePageAbout(models.Model):
    homepage_about_title = models.CharField(max_length=100, blank=False, null=False)
    homepage_about_lead = models.CharField(max_length=200, blank=False, null=False)
    homepage_about_subtitle = models.CharField(max_length=100, blank=False, null=False)
    homepage_about_paragraph_one = models.TextField(blank=False, null=False)
    homepage_about_paragraph_two = models.TextField(blank=False, null=False)
    homepage_about_image = models.ImageField(upload_to="cms/home/")

    def __str__(self):
        return f"{self.homepage_about_title} - {self.homepage_about_subtitle}"
        