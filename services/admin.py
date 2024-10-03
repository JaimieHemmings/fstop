from django.contrib import admin
from .models import (
  ServicesHero,
  ServicesBanner,
  ServicesCards,
  ServicesContextBannerOne,
  ServicesContextBannerTwo,
  )


class ServicesHeroAdmin(admin.ModelAdmin):
    pass


class ServicesBannerAdmin(admin.ModelAdmin):
    pass


class ServicesCardsAdmin(admin.ModelAdmin):
    pass


class ServicesContextBannerOneAdmin(admin.ModelAdmin):
    pass


class ServicesContextBannerTwoAdmin(admin.ModelAdmin):
    pass


admin.site.register(ServicesHero, ServicesHeroAdmin)
admin.site.register(ServicesBanner, ServicesBannerAdmin)
admin.site.register(ServicesCards, ServicesCardsAdmin)
admin.site.register(
                    ServicesContextBannerOne,
                    ServicesContextBannerOneAdmin
                    )
admin.site.register(
                    ServicesContextBannerTwo,
                    ServicesContextBannerTwoAdmin
                    )
