from django.shortcuts import render

def blog(request):
    """
    A view to return the blog page
    """
    return render(request, 'blog.html')

def article(request, slug):
    return render(request, 'article.html')