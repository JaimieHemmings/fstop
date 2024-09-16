from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField()
    body_continued = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    cover_image = models.ImageField(default='default.png', blank=True)
    body_image = models.ImageField(default='default.png', blank=True)
    last_modified = models.DateTimeField(auto_now=True)