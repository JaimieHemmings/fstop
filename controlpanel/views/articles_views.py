from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.template.defaultfilters import slugify
from django.utils import timezone

from blog.models import Article
from home.models import Message
from controlpanel.forms import CreateArticleForm


@user_passes_test(lambda u: u.is_superuser)
def cp_articles(request):
    """
    A view to return the articles page
    """
    latest_messages = Message.objects.all().order_by("-created_at")[:5]
    total_unread_messages = Message.objects.filter(read=False).count()
    articles = Article.objects.all()
    unread_messages = Message.objects.filter(read=False)[:5]

    context = {
        "articles": articles,
        "latest_messages": latest_messages,
        "total_unread_messages": total_unread_messages,
        "unread_messages": unread_messages,
    }
    return render(request, "article-management.html", context)


@user_passes_test(lambda u: u.is_superuser)
def add_article(request):
    """
    A view to add an article
    """
    latest_messages = Message.objects.all().order_by("-created_at")[:5]
    total_unread_messages = Message.objects.filter(read=False).count()
    unread_messages = Message.objects.filter(read=False)[:5]

    context = {
        latest_messages: latest_messages,
        total_unread_messages: total_unread_messages,
        unread_messages: unread_messages
    }
    form = CreateArticleForm()
    if request.method == "POST":
        form = CreateArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.slug = slugify(article.title)
            article.save()
            messages.success(request, "Article created successfully")
            return cp_articles(request)
    context["form"] = form
    context["page_title"] = "Add Article"
    context["end_point"] = "add_article"
    return render(request, "generic/add-item.html", context)


@user_passes_test(lambda u: u.is_superuser)
def edit_article(request, article_id):
    """
    A view to edit an article
    """
    latest_messages = Message.objects.all().order_by("-created_at")[:5]
    total_unread_messages = Message.objects.filter(read=False).count()
    unread_messages = Message.objects.filter(read=False)[:5]

    context = {}

    article = Article.objects.get(id=article_id)
    form = CreateArticleForm(instance=article)
    if request.method == "POST":
        form = CreateArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.slug = slugify(article.title)
            article.last_modified = timezone.now()
            article.save()
            messages.success(request, "Article updated successfully")
            return cp_articles(request)

    context = {
        "end_point": "edit_article",
        "item": article,
        "article": article,
        "form": form,
        "unread_messages": unread_messages,
        "total_unread_messages": total_unread_messages,
        "latest_messages": latest_messages,
    }

    return render(request, "generic/edit-item.html", context)


@user_passes_test(lambda u: u.is_superuser)
def delete_article_confirm(request, article_id):
    """
    A view to confirm the deletion of an article
    """
    latest_messages = Message.objects.all().order_by("-created_at")[:5]
    total_unread_messages = Message.objects.filter(read=False).count()
    unread_messages = Message.objects.filter(read=False)[:5]

    context = {
        "latest_messages": latest_messages,
        "total_unread_messages": total_unread_messages,
        "unread_messages": unread_messages,
        "return_path": "cp_articles",
        "delete_path": "delete_article"
    }
    article = Article.objects.get(id=article_id)
    context["item"] = article
    return render(request, "generic/delete-confirmation.html", context)


@user_passes_test(lambda u: u.is_superuser)
def delete_article(request, article_id):
    """
    A view to delete an article
    """
    article = Article.objects.get(id=article_id)
    article.delete()
    messages.success(request, "Article deleted successfully")
    return cp_articles(request)

