from django.db import models
import uuid


class Article(models.Model):
    def get_path(self, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return f'blog_images/{filename}'

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    exerpt = models.CharField(max_length=255)
    body = models.TextField()
    body_continued = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(
        upload_to=get_path, default="default.png")
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    slider_image_one = models.ImageField(
        upload_to=get_path, default="default.png")
    slider_image_two = models.ImageField(
        upload_to=get_path, default="default.png")
    slider_image_three = models.ImageField(
        upload_to=get_path, default="default.png")
    slider_image_four = models.ImageField(
        upload_to=get_path, default="default.png")
    body_image = models.ImageField(
        upload_to=get_path, default="default.png")
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
