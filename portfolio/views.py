from django.shortcuts import render

def portfolio(request):
    """
    A view to return the portfolio page
    """
    context = {}
    return render(request, 'portfolio.html', context)
