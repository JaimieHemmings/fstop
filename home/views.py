from django.shortcuts import render

def index(request):
    """
    A view that displays the index page
    """
    return render(request, 'home/index.html')

def about(request):
    """
    A view that displays the about page
    """
    return render(request, 'home/about.html')

def contact(request):
    """
    A view that displays the contact page
    """
    return render(request, 'home/contact.html')
