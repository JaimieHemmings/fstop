from django.contrib import admin
from blog.models import Article
from portfolio.models import PortfolioImages, SliderImages
from .models import Message
from reviews.models import Review
from payments.models import Payment

class MessageAdmin(admin.ModelAdmin):
    pass

class ArticleAdmin(admin.ModelAdmin):
    pass

class PortfolioImagesAdmin(admin.ModelAdmin):
    pass

class SliderImagesAdmin(admin.ModelAdmin):
    pass

class ReviewAdmin(admin.ModelAdmin):
    pass

class PaymentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Message, MessageAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(PortfolioImages, PortfolioImagesAdmin)
admin.site.register(SliderImages, SliderImagesAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Payment, PaymentAdmin)
