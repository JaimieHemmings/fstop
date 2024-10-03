from django.shortcuts import render
from .models import (
  ServicesHero,
  ServicesBanner,
  ServicesCards,
  ServicesContextBannerOne,
  ServicesContextBannerTwo
  )

def services(request):
    """
    A view to return the services page
    """
    services_hero = ServicesHero.objects.get(id=1)
    services_banner = ServicesBanner.objects.get(id=1)
    services_cards = ServicesCards.objects.all()
    services_context_banner_one = (
        ServicesContextBannerOne.objects.get(id=1)
    )
    services_context_banner_two = (
        ServicesContextBannerTwo.objects.get(id=1)
    )

    context = {
        "services_hero": services_hero,
        "services_banner": services_banner,
        "services_cards": services_cards,
        "services_context_banner_one": (
            services_context_banner_one
        ),
        "services_context_banner_two": (
            services_context_banner_two
        )
    }


    return render(request, "services/services.html", context)
