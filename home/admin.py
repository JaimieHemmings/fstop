from django.contrib import admin
from blog.models import Article
from portfolio.models import PortfolioImages
from .models import (
  Message,
  HomePageHero,
  HomePageAbout,
  HomePageTrustedBy,
  HomePageFAQs,
  HomePageSliderImages)

from reviews.models import Review
from payments.models import Payment


class MessageAdmin(admin.ModelAdmin):
    pass


class ArticleAdmin(admin.ModelAdmin):
    pass


class PortfolioImagesAdmin(admin.ModelAdmin):
    pass


class HomePageSliderImagesAdmin(admin.ModelAdmin):
    pass


class ReviewAdmin(admin.ModelAdmin):
    pass


class PaymentAdmin(admin.ModelAdmin):
    pass


class HomePageHeroAdmin(admin.ModelAdmin):
    pass


class HomePageAboutAdmin(admin.ModelAdmin):
    pass


class HomePageTrustedByAdmin(admin.ModelAdmin):
    pass


class HomePageFAQsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Message, MessageAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(PortfolioImages, PortfolioImagesAdmin)
admin.site.register(HomePageSliderImages, HomePageSliderImagesAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(HomePageHero, HomePageHeroAdmin)
admin.site.register(HomePageAbout, HomePageAboutAdmin)
admin.site.register(HomePageTrustedBy, HomePageTrustedByAdmin)
admin.site.register(HomePageFAQs, HomePageFAQsAdmin)