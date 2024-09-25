from django.shortcuts import render
from .models import PortfolioImages


def portfolio(request):
    """
    A view to return the portfolio page
    """
    context = {}
    # Get all portfolio images
    portfolio_images = PortfolioImages.objects.all()
    context["portfolio_images"] = portfolio_images

    return render(request, "portfolio.html", context)
