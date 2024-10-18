from django.shortcuts import render
from .models import Article


def blog(request):
    """
    A view to return the blog page
    """
    # Get all articles and order by date
    articles = Article.objects.all().order_by("-date")
    context = {
        "articles": articles,
    }
    return render(request, "blog.html", context)


def article(request, slug):
    """
    A view to return the article page
    """
    # Get the article by slug
    article = Article.objects.get(slug=slug)
    context = {
        "article": article,
    }
    # Incerement the view count
    article.views += 1
    article.save()
    return render(request, "article.html", context)
