from django.db import models


# Create your models here.
class PortfolioImages(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to="portfolio/", blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.created_at.strftime('%d/%m/%Y %H:%M')}"
