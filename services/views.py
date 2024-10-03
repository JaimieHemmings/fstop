from django.shortcuts import render, get_object_or_404
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
    services_hero = get_object_or_404(ServicesHero, id=1)
    services_banner = get_object_or_404(ServicesBanner, id=1)
    services_cards = ServicesCards.objects.all()
    services_context_banner_one = (
        get_object_or_404(ServicesContextBannerOne, id=1)
    )
    services_context_banner_two = (
        get_object_or_404(ServicesContextBannerTwo, id=1)
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
