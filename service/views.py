from django.shortcuts import render, get_object_or_404
from home.models import HomePageTrustedBy
from .models import ServicesPage


def services(request):
    # Redirect to the 404 page
    return render(request, "404.html")


def lifestyle_services(request):
    homepage_trusted_by = get_object_or_404(HomePageTrustedBy, id=1)
    page_info = get_object_or_404(ServicesPage, title="Lifestyle")

    context = {
        "homepage_trusted_by": homepage_trusted_by,
        "page_info": page_info,
    }
    return render(request, "services/service-template.html", context)


def event_services(request):
    homepage_trusted_by = get_object_or_404(HomePageTrustedBy, id=1)
    page_info = get_object_or_404(ServicesPage, title="Event")

    context = {
        "page_info": page_info,
        "homepage_trusted_by": homepage_trusted_by,
    }
    return render(request, "services/service-template.html", context)


def property_services(request):
    page_info = get_object_or_404(ServicesPage, title="Property")
    homepage_trusted_by = get_object_or_404(HomePageTrustedBy, id=1)

    context = {
        "page_info": page_info,
        "homepage_trusted_by": homepage_trusted_by,
    }
    return render(request, "services/service-template.html", context)


def aerial_services(request):
    page_info = get_object_or_404(ServicesPage, title="Aerial")
    homepage_trusted_by = get_object_or_404(HomePageTrustedBy, id=1)

    context = {
        "page_info": page_info,
        "homepage_trusted_by": homepage_trusted_by,
    }
    return render(request, "services/service-template.html", context)
