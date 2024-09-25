from django.shortcuts import render
from .models import Article


def blog(request):
    """
    A view to return the blog page
    """
    context = {}
    articles = Article.objects.all().order_by("-date")
    context["articles"] = articles

    return render(request, "blog.html", context)


def article(request, slug):
    """
    A view to return the article page
    """
    context = {}
    article = Article.objects.get(slug=slug)
    context["article"] = article

    return render(request, "article.html", context)
