from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    content = models.TextField()
    user_img = models.ImageField(upload_to='reviews', default='default.png')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
