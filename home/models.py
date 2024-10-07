from django.db import models
import uuid

class Message(models.Model):
    fname = models.CharField(max_length=100, blank=False, null=False)
    lname = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return (
            f"{self.fname} {self.lname} -"
            " {self.created_at.strftime('%d/%m/%Y %H:%M')}"
        )


class HomePageHero(models.Model):

    def get_path(instance, filename):
        extension = filename.split(".")[-1]
        filename = f"{filename}-{uuid.uuid4()}.{extension}"
        return f"cms/home/{filename}"
    
    hero_title = models.CharField(max_length=50, blank=False, null=False)
    hero_subtitle = models.TextField(max_length=200, blank=False, null=False)
    hero_image = models.ImageField(upload_to=get_path)
    hero_image_alt = models.CharField(max_length=100, blank=False, null=False, default="Enter an alt text")
    hero_image_mobile = models.ImageField(upload_to=get_path, default="default.png")
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
    homepage_about_title = models.CharField(
        max_length=100, blank=False, null=False, default="Enter a Title")
    homepage_about_lead = models.CharField(
        max_length=200, blank=False, null=False, default="Enter a Lead")
    homepage_about_subtitle = models.CharField(
        max_length=100, blank=False, null=False, default="Enter a Subtitle")
    homepage_about_paragraph_one = models.TextField(
        blank=False, null=False, default="Enter a Paragraph")
    homepage_about_paragraph_two = models.TextField(
        blank=False, null=False, default="Enter a Paragraph")
    homepage_about_image = models.ImageField(
        upload_to="cms/home/", default="default.png")

    def __str__(self):
        return f"{self.homepage_about_title}"


class HomePageTrustedBy(models.Model):
    trusted_by_title = models.CharField(
        max_length=100, blank=False, null=False, default="Enter a Title")
    trusted_by_lead = models.CharField(
        max_length=200, blank=False, null=False, default="Enter a Lead")
    img_one = models.ImageField(upload_to="cms/home/", default="default.png")
    img_two = models.ImageField(upload_to="cms/home/", default="default.png")
    img_three = models.ImageField(upload_to="cms/home/", default="default.png")
    img_four = models.ImageField(upload_to="cms/home/", default="default.png")
    img_five = models.ImageField(upload_to="cms/home/", default="default.png")
    img_six = models.ImageField(upload_to="cms/home/", default="default.png")
    img_seven = models.ImageField(upload_to="cms/home/", default="default.png")
    img_eight = models.ImageField(upload_to="cms/home/", default="default.png")

    def __str__(self):
        return f"{ self.trusted_by_title }"
    

class HomePageFAQ(models.Model):
    faq_question = models.CharField(max_length=100, blank=False, null=False)
    faq_answer = models.TextField(blank=False, null=False)

    def __str__(self):
        return f"{self.faq_question}"


class HomePageSliderImages(models.Model):
    """
    Generate a unique path for each image uploaded to the slider

    :param instance: The instance of the model
    :param filename: The name of the file being uploaded
    :return: The path for the image
    rtype: str
    """
    def get_path(instance, filename):
        extension = filename.split(".")[-1]
        filename = f"{filename}-{uuid.uuid4()}.{extension}"
        return f"slider-images/{filename}"

    title = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to=get_path, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
    

class HomePagePanel(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    icon = models.CharField(max_length=1000, blank=False, null=False)
    paragraph = models.TextField(blank=False, null=False)

    def __str__(self):
        return f"{self.title}"