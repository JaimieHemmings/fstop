from django.contrib import admin
from .models import ServicesPage


class ServicesPageAdmin(admin.ModelAdmin):
    pass


admin.site.register(ServicesPage, ServicesPageAdmin)
