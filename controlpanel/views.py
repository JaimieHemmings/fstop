from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.utils import timezone
from blog.models import Article
from home.models import Message
from portfolio.models import PortfolioImages, SliderImages
from .forms import CreateArticleForm, AddSliderImage, AddPortfolioImage


"""
This file contains the views for the control panel
All views require the user to be logged in and a superuser
"""


@login_required
@user_passes_test(lambda u: u.is_superuser)
def control_panel(request):
    """
    A view to return the control panel page
    """
    context = {}

    # Get the number of registered users
    number_of_users = User.objects.all().count()
    context["number_of_users"] = number_of_users

    number_of_articles = Article.objects.all().count()
    context["number_of_articles"] = number_of_articles

    latest_articles = Article.objects.all().order_by('-date')[:5]
    context["latest_articles"] = latest_articles

    latest_users = User.objects.all().order_by('-date_joined')[:5]
    context["latest_users"] = latest_users

    # Get the lastest messages
    latest_messages = Message.objects.all().order_by('-created_at')[:5]
    context["latest_messages"] = latest_messages

    # Get the number of unread messages
    unread_messages = Message.objects.filter(read=False).count()
    context["unread_messages"] = unread_messages

    return render(request, 'control-panel.html', context)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def cp_articles(request):
    """
    A view to return the articles page
    """
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'articles/article-management.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def cp_messages(request):
    """
    A view to return the messages page
    """
    messages = Message.objects.all()

    context = {
        'formMessages': messages,
    }

    return render(request, 'messages/message-management.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def toggle_read(request, message_id):
    """
    A view to toggle the read status of a message
    """
    message = Message.objects.get(id=message_id)
    message.read = not message.read
    message.save()
    messages.success(request, 'Message status updated successfully')

    return cp_messages(request)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_message_confirm(request, message_id):
    """
    A view to confirm the deletion of a message
    """
    context = {}
    message = Message.objects.get(id=message_id)
    context['message'] = message


    return render(request, 'messages/delete-message-confirm.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_message(request, message_id):
    """
    A view to delete a message
    """
    message = Message.objects.get(id=message_id)
    message.delete()
    messages.success(request, 'Message deleted successfully')

    return cp_messages(request)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def add_article(request):
    """
    A view to add an article
    """
    context = {}

    form = CreateArticleForm()
    context['form'] = form

    if request.method == 'POST':
        form = CreateArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.slug = slugify(article.title)
            article.save()
            messages.success(request, 'Article created successfully')
            return cp_articles(request)
        else:
            context['form'] = form

    return render(request, 'articles/create-article.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit_article(request, article_id):
    """
    A view to edit an article
    """
    context = {}

    article = Article.objects.get(id=article_id)
    form = CreateArticleForm(instance=article)
    context['article'] = article
    context['form'] = form

    if request.method == 'POST':
        form = CreateArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.slug = slugify(article.title)
            article.last_modified = timezone.now()
            article.save()
            messages.success(request, 'Article updated successfully')
            return cp_articles(request)
        else:
            context['form'] = form

    return render(request, 'articles/edit-article.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_article_confirm(request, article_id):
    """
    A view to confirm the deletion of an article
    """
    context = {}
    article = Article.objects.get(id=article_id)
    context['article'] = article

    # Redirect back to Articles Management page
    return render(request, 'articles/confirm-delete-article.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_article(request, article_id):
    """
    A view to delete an article
    """
    article = Article.objects.get(id=article_id)
    article.delete()
    messages.success(request, 'Article deleted successfully')

    return cp_articles(request)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def cp_portfolio(request):
    """
    A view to return the portfolio page
    """
    context = {}
    sliderImages = SliderImages.objects.all()
    context['sliderImages'] = sliderImages
    portfolioImages = PortfolioImages.objects.all()
    context['portfolioImages'] = portfolioImages

    return render(request, 'portfolio/portfolio-management.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def add_slider_image(request):
    """
    A view to add a slider image
    """
    context = {}

    form = AddSliderImage()
    context['form'] = form

    if request.method == 'POST':
        num_of_slider_images = SliderImages.objects.all().count()
        if num_of_slider_images < 9:
            form = AddSliderImage(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Slider image added successfully')
                return redirect(cp_portfolio)
            else:
                context['form'] = form
        else:
            messages.error(request, 'You can only have a maximum of 9 slider images')
            return redirect(cp_portfolio)

    return render(request, 'portfolio/add-slider-image.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def add_portfolio_image(request):
    """
    A view to add a slider image
    """
    context = {}

    form = AddPortfolioImage()
    context['form'] = form

    if request.method == 'POST':
        form = AddPortfolioImage(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Portfolio image added successfully')
            return redirect(cp_portfolio)
        else:
            context['form'] = form

    return render(request, 'portfolio/add-portfolio-image.html', context)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_slider_image_confirm(request, image_id):
    """
    A view to confirm the deletion of a slider image
    """
    context = {}
    image = SliderImages.objects.get(id=image_id)
    context['image'] = image

    return render(request, 'portfolio/delete-slider-image-confirm.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_portfolio_image_confirm(request, image_id):
    """
    A view to confirm the deletion of a portfolio image
    """
    context = {}
    image = PortfolioImages.objects.get(id=image_id)
    context['image'] = image

    return render(request, 'portfolio/delete-portfolio-image-confirm.html', context)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_slider_image(request, image_id):
    """
    A view to delete a slider image
    """
    image = SliderImages.objects.get(id=image_id)
    image.delete()
    messages.success(request, 'Slider image deleted successfully')

    return redirect(cp_portfolio)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_portfolio_image(request, image_id):
    """
    A view to delete a portfolio image
    """
    image = PortfolioImages.objects.get(id=image_id)
    image.delete()
    messages.success(request, 'Portfolio image deleted successfully')

    return redirect(cp_portfolio)

