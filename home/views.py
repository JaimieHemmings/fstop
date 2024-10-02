from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from blog.models import Article
from reviews.models import Review
from .models import (
    HomePageHero,
    HomePageAbout,
    HomePageTrustedBy,
    HomePageFAQ,
    HomePageSliderImages,
    HomePagePanel
  )


def index(request):
    """
    A view that displays the index page
    """
    # Get objects
    homepage_hero = HomePageHero.objects.get(id=1)
    homepage_about = HomePageAbout.objects.get(id=1)
    homepage_trusted_by = HomePageTrustedBy.objects.get(id=1)
    homepage_faqs = HomePageFAQ.objects.all()
    homepage_slider_images = HomePageSliderImages.objects.all()
    homepage_panels = HomePagePanel.objects.all()

    articles = Article.objects.all().order_by("-date")[:2]
    reviews = Review.objects.all().order_by("-created_at")[:5]
    # Build context
    context = {
        "articles": articles,
        "reviews": reviews,
        "homepage_hero": homepage_hero,
        "homepage_about": homepage_about,
        "homepage_trusted_by": homepage_trusted_by,
        "homepage_faqs": homepage_faqs,
        "homepage_slider_images": homepage_slider_images,
        "homepage_panels": homepage_panels,
    }
    return render(request, "home/index.html", context)


def about(request):
    """
    A view that displays the about page
    """
    context = {}
    # Get the 2 latest Articles
    articles = Article.objects.all().order_by("-date")[:2]
    context["articles"] = articles

    return render(request, "home/about.html")


def contact(request):
    """
    A view that displays the contact page
    """
    context = {}
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Flash Message confirmation
            messages.success(request, "Your message has been sent!")
        else:
            # Flash Message error
            messages.error(request, "Error sending message. Please check the form.")
    context["form"] = form
    return render(request, "home/contact.html", context)
