from django.shortcuts import render, get_object_or_404
from django.http import Http404
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
    HomePagePanel,
    AboutPage,
  )

def get_all_or_404(model):
    """
    Get all objects of a model or return 404
    """
    objects = model.objects.all()
    if not objects.exists():
        raise Http404(f"No {model._meta.verbose_name_plural} found")
    return objects


def index(request):
    """
    A view that displays the index page
    """
    # Get objects
    homepage_hero = get_object_or_404(HomePageHero, id=1)
    homepage_about = get_object_or_404(HomePageAbout, id=1)
    homepage_trusted_by = get_object_or_404(HomePageTrustedBy, id=1)
    homepage_faqs = get_all_or_404(HomePageFAQ)
    homepage_slider_images = get_all_or_404(HomePageSliderImages)
    homepage_panels = get_all_or_404(HomePagePanel)
    articles = get_all_or_404(Article)
    articles = articles.order_by("-date")[:2]
    reviews = get_all_or_404(Review)
    reviews = reviews.order_by("-created_at")[:5]
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
    page_info = get_object_or_404(AboutPage, title="About")
    context = {"page_info": page_info}
    return render(request, "home/about.html", context)


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
            messages.error(
                request,
                "Error sending message. Please check the form.")
    context["form"] = form
    return render(request, "home/contact.html", context)
