from django.contrib import admin
from blog.models import Article
from portfolio.models import PortfolioImages
from .models import (
  Message,
  HomePageHero,
  HomePageAbout,
  HomePageTrustedBy,
  HomePageFAQ,
  HomePageSliderImages,
  HomePagePanel)

from reviews.models import Review


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


class HomePageHeroAdmin(admin.ModelAdmin):
    pass


class HomePageAboutAdmin(admin.ModelAdmin):
    pass


class HomePageTrustedByAdmin(admin.ModelAdmin):
    pass


class HomePageFAQAdmin(admin.ModelAdmin):
    pass

class HomePagePanelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Message, MessageAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(PortfolioImages, PortfolioImagesAdmin)
admin.site.register(HomePageSliderImages, HomePageSliderImagesAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(HomePageHero, HomePageHeroAdmin)
admin.site.register(HomePageAbout, HomePageAboutAdmin)
admin.site.register(HomePageTrustedBy, HomePageTrustedByAdmin)
admin.site.register(HomePageFAQ, HomePageFAQAdmin)
admin.site.register(HomePagePanel, HomePagePanelAdmin)