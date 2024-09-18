from django.shortcuts import render
from .models import PortfolioImages

def portfolio(request):
    """
    A view to return the portfolio page
    """
    context = {}
    #Get all portfolio images
    portfolioImages = PortfolioImages.objects.all()
    context['portfolioImages'] = portfolioImages

    return render(request, 'portfolio.html', context)
