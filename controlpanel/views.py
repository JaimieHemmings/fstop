from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.urls import reverse

from blog.models import Article
from home.models import (
  Message,
  HomePageHero,
  HomePageAbout,
  HomePageTrustedBy,
  HomePageFAQ,
  HomePagePanel
)
from portfolio.models import PortfolioImages
from home.models import HomePageSliderImages
from reviews.models import Review
from payments.models import Payment
from services.models import (
    ServicesHero,
    ServicesBanner,
    ServicesCards,
    ServicesContextBannerOne,
    ServicesContextBannerTwo,
)

from .forms import CreateArticleForm
from home.forms import AddSliderImageForm
from .forms import AddPortfolioImage, AddReviewForm
from .forms import NewPaymentForm
from home.forms import (
  HomeHeroForm,
  editAboutSectionHomeForm,
  HomePageTrustedByForm,
  HomePageFAQForm,
  AddHomePagePanelForm
)
from services.forms import (
  ServicesHeroForm,
  ServicesBannerForm,
  ServicesCardsForm,
)


@user_passes_test(lambda u: u.is_superuser)
def control_panel(request):
    """
    A view to return the control panel page
    """
    latest_messages = Message.objects.all().order_by("-created_at")[:5]
    total_unread_messages = Message.objects.filter(read=False).count()
    total_num_users = User.objects.all().count()
    total_articles = Article.objects.all().count()
    unread_messages = Message.objects.filter(read=False)[:5]

    latest_articles = Article.objects.all().order_by("-date")[:5]
    latest_users = User.objects.all().order_by("-date_joined")[:5]
    latest_reviews = Review.objects.all().order_by("-created_at")[:5]
    latest_payment_requests = Payment.objects.all().order_by("-date")[:5]
    # Build context
    context = {
        "total_num_users": total_num_users,
        "total_articles": total_articles,
        "latest_articles": latest_articles,
        "latest_users": latest_users,
        "latest_messages": latest_messages,
        "total_unread_messages": total_unread_messages,
        "unread_messages": unread_messages,
        "latest_reviews": latest_reviews,
        "latest_payment_requests": latest_payment_requests,
    }
    return render(request, "control-panel.html", context)


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
    return render(request, "articles/article-management.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cp_messages(request):
    """
    A view to return the messages page
    """
    latest_messages = Message.objects.all().order_by("-created_at")[:5]
    total_unread_messages = Message.objects.filter(read=False).count()
    unread_messages = Message.objects.filter(read=False)[:5]
    messages = Message.objects.all()

    context = {
        "form_messages": messages,
        "latest_messages": latest_messages,
        "total_unread_messages": total_unread_messages,
        "unread_messages": unread_messages,
    }
    return render(request, "messages/message-management.html", context)


@user_passes_test(lambda u: u.is_superuser)
def view_message(request, message_id):
    """
    A view to view a message
    """
    message = Message.objects.get(id=message_id)
    message.read = True
    message.save()
    total_unread_messages = Message.objects.filter(read=False).count()
    unread_messages = Message.objects.filter(read=False)[:5]

    context = {
        "message": message,
        "total_unread_messages": total_unread_messages,
        "unread_messages": unread_messages,
    }
    return render(request, "messages/view-message.html", context)


@user_passes_test(lambda u: u.is_superuser)
def toggle_read(request, message_id):
    """
    A view to toggle the read status of a message
    """
    try:
        message = Message.objects.get(id=message_id)
        message.read = not message.read
        message.save()
        messages.success(request, "Message status updated successfully")
    except Message.DoesNotExist:
        messages.error(request, "Message not found")
    return redirect(reverse(cp_messages))


@user_passes_test(lambda u: u.is_superuser)
def delete_message_confirm(request, message_id):
    """
    A view to confirm the deletion of a message
    """
    latest_messages = Message.objects.all().order_by("-created_at")[:5]
    total_unread_messages = Message.objects.filter(read=False).count()
    message = Message.objects.get(id=message_id)
    unread_messages = Message.objects.filter(read=False)[:5]

    context = {
        "message": message,
        "latest_messages": latest_messages,
        "total_unread_messages": total_unread_messages,
        "unread_messages": unread_messages,
    }
    return render(request, "messages/delete-message-confirm.html", context)


@user_passes_test(lambda u: u.is_superuser)
def delete_message(request, message_id):
    """
    A view to delete a message
    """
    message = Message.objects.get(id=message_id)
    message.delete()
    messages.success(request, "Message deleted successfully")
    return cp_messages(request)


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
    return render(request, "articles/create-article.html", context)


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

    context["article"] = article
    context["latest_messages"] = latest_messages
    context["total_unread_messages"] = total_unread_messages
    context["unread_messages"] = unread_messages
    context["form"] = form

    return render(request, "articles/edit-article.html", context)


@user_passes_test(lambda u: u.is_superuser)
def delete_article_confirm(request, article_id):
    """
    A view to confirm the deletion of an article
    """
    latest_messages = Message.objects.all().order_by("-created_at")[:5]
    total_unread_messages = Message.objects.filter(read=False).count()
    unread_messages = Message.objects.filter(read=False)[:5]

    context = {
        latest_messages: latest_messages,
        total_unread_messages: total_unread_messages,
        unread_messages: unread_messages
    }
    article = Article.objects.get(id=article_id)
    context["article"] = article
    return render(request, "articles/confirm-delete-article.html", context)


@user_passes_test(lambda u: u.is_superuser)
def delete_article(request, article_id):
    """
    A view to delete an article
    """
    article = Article.objects.get(id=article_id)
    article.delete()
    messages.success(request, "Article deleted successfully")
    return cp_articles(request)


@user_passes_test(lambda u: u.is_superuser)
def cp_portfolio(request):
    """
    A view to return the portfolio page
    """
    context = {}
    slider_images = HomePageSliderImages.objects.all()
    context["slider_images"] = slider_images
    portfolio_images = PortfolioImages.objects.all()
    context["portfolio_images"] = portfolio_images
    return render(request, "portfolio/portfolio-management.html", context)


@user_passes_test(lambda u: u.is_superuser)
def add_portfolio_image(request):
    """
    A view to add a slider image
    """
    context = {}
    form = AddPortfolioImage()
    if request.method == "POST":
        form = AddPortfolioImage(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Portfolio image added successfully")
            return redirect(cp_portfolio)
    context["form"] = form
    return render(request, "portfolio/add-portfolio-image.html", context)


@user_passes_test(lambda u: u.is_superuser)
def delete_portfolio_image_confirm(request, image_id):
    """
    A view to confirm the deletion of a portfolio image
    """
    context = {}
    image = PortfolioImages.objects.get(id=image_id)
    context["image"] = image

    return render(
        request, "portfolio/delete-portfolio-image-confirm.html", context)


@user_passes_test(lambda u: u.is_superuser)
def delete_portfolio_image(request, image_id):
    """
    A view to delete a portfolio image
    """
    image = PortfolioImages.objects.get(id=image_id)
    image.delete()
    messages.success(request, "Portfolio image deleted successfully")
    return redirect(cp_portfolio)


@user_passes_test(lambda u: u.is_superuser)
def cp_payments(request):
    """
    A view to return the payments page
    """
    payments = Payment.objects.all()
    context = {
        "payments": payments,
    }
    return render(request, "payments/payment-management.html", context)


@user_passes_test(lambda u: u.is_superuser)
def new_payment(request):
    """
    A view to add a payment
    """
    form = NewPaymentForm()
    if request.method == "POST":
        form = NewPaymentForm(request.POST)
        if form.is_valid():
            # Use the email address to get the users name
            email = form.cleaned_data["email"]
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                messages.error(
                    request, "No user found with that email address")
                context = {
                    "form": form,
                }
                return render(request, "payments/new-payment.html", context)
            name = user.first_name + " " + user.last_name
            form.instance.name = name
            form.save()
            messages.success(request, "Payment request added successfully")
            return redirect(cp_payments)
    context = {
        "form": form,
    }
    return render(request, "payments/new-payment.html", context)


@user_passes_test(lambda u: u.is_superuser)
def view_payment(request, payment_id):
    """
    A view to view the details of a payment
    """
    payment = Payment.objects.get(id=payment_id)
    context = {
        "payment": payment,
    }
    return render(request, "payments/view-payment.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cp_analytics(request):
    """
    A view to return the analytics page
    """
    return render(request, "analytics/analytics.html")


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_home(request):
    """
    A view to return the CMS homepage
    """
    unread_messages = Message.objects.filter(read=False)[:5]
    total_unread_messages = Message.objects.filter(read=False).count()

    context = {
        "unread_messages": unread_messages,
        "total_unread_messages": total_unread_messages,
    }
    return render(request, "cms/cms-homepage.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_hero(request):
    """
    A view to return the CMS homepage
    """
    home_hero_data = HomePageHero.objects.get(id=1)
    form = HomeHeroForm(instance=home_hero_data)
    unread_messages = Message.objects.filter(read=False)[:5]
    total_unread_messages = Message.objects.filter(read=False).count()

    if request.method == "POST":
        form = HomeHeroForm(
            request.POST, request.FILES, instance=home_hero_data)
        if form.is_valid():
            form.save()
            messages.success(request, "Homepage data updated successfully")
        else:
            messages.error(
                request, "There was an error updating the homepage data")

    context = {
        "form": form,
        "unread_messages": unread_messages,
        "total_unread_messages": total_unread_messages,
    }

    return render(request, "cms/home/cms-edit-hero.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_about_home_edit(request):
    """
    A view to return the CMS homepage about page
    """
    about_data = HomePageAbout.objects.get(id=1)
    form = editAboutSectionHomeForm(instance=about_data)
    unread_messages = Message.objects.filter(read=False)[:5]
    total_unread_messages = Message.objects.filter(read=False).count()

    if request.method == "POST":
        form = editAboutSectionHomeForm(
            request.POST, request.FILES, instance=about_data)
        if form.is_valid():
            form.save()
            messages.success(request, "Homepage data updated successfully")
        else:
            messages.error(
                request, "There was an error updating the homepage data")

    context = {
        "form": form,
        "unread_messages": unread_messages,
        "total_unread_messages": total_unread_messages,
    }

    return render(request, "cms/home/cms-edit-about-home.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_trusted_by_edit(request):
    """
    A view to return the CMS homepage about page
    """
    unread_messages = Message.objects.filter(read=False)[:5]
    total_unread_messages = Message.objects.filter(read=False).count()
    trusted_by_data = HomePageTrustedBy.objects.get(id=1)
    form = HomePageTrustedByForm(instance=trusted_by_data)

    context = {
        "unread_messages": unread_messages,
        "total_unread_messages": total_unread_messages,
        "form": form,
    }

    if request.method == "POST":
        form = HomePageTrustedByForm(
            request.POST, request.FILES, instance=trusted_by_data)
        if form.is_valid():
            form.save()
            messages.success(request, "Homepage data updated successfully")
        else:
            messages.error(
                request, "There was an error updating the homepage data")

    return render(request, "cms/home/cms-edit-trusted-by.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_faq(request):
    """
    A view to return the CMS homepage about page
    """
    unread_messages = Message.objects.filter(read=False)[:5]
    total_unread_messages = Message.objects.filter(read=False).count()
    faqs = HomePageFAQ.objects.all()
    context = {
        "unread_messages": unread_messages,
        "total_unread_messages": total_unread_messages,
        "faqs": faqs,
    }
    return render(request, "cms/faqs/cms-faqs.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cms_add_faq(request):
    """
    A view to add a FAQ
    """
    unread_messages = Message.objects.filter(read=False)[:5]
    total_unread_messages = Message.objects.filter(read=False).count()
    context = {
        "unread_messages": unread_messages,
        "total_unread_messages": total_unread_messages,
    }
    form = HomePageFAQForm()
    if request.method == "POST":
        form = HomePageFAQForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "FAQ added successfully")
            return redirect(cp_cms_faq)
    context["form"] = form
    return render(request, "cms/faqs/cms-add-faq.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cms_edit_faq(request, faq_id):
    """
    A view to edit a FAQ
    """
    unread_messages = Message.objects.filter(read=False)[:5]
    total_unread_messages = Message.objects.filter(read=False).count()
    context = {
        "unread_messages": unread_messages,
        "total_unread_messages": total_unread_messages,
    }
    faq = HomePageFAQ.objects.get(id=faq_id)
    form = HomePageFAQForm(instance=faq)
    context["faq"] = faq
    if request.method == "POST":
        form = HomePageFAQForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            messages.success(request, "FAQ updated successfully")
            return redirect(cp_cms_faq)
    context["form"] = form
    return render(request, "cms/faqs/cms-edit-faq.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cms_delete_faq_confirm(request, faq_id):
    """
    A view to confirm the deletion of a FAQ
    """
    unread_messages = Message.objects.filter(read=False)[:5]
    total_unread_messages = Message.objects.filter(read=False).count()

    faq = HomePageFAQ.objects.get(id=faq_id)

    context = {
        "unread_messages": unread_messages,
        "total_unread_messages": total_unread_messages,
        "faq": faq,
    }
    return render(request, "cms/faqs/cms-faq-confirm-delete.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cms_delete_faq(request, faq_id):
    """
    A view to delete a FAQ
    """
    faq = HomePageFAQ.objects.get(id=faq_id)
    faq.delete()
    messages.success(request, "FAQ deleted successfully")
    return redirect(cp_cms_faq)


"""
Homepage Slider Images Management
"""


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_manage_slider_images(request):
    """
    A view to return the CMS homepage slider images page
    """
    unread_messages = Message.objects.filter(read=False)[:5]
    total_unread_messages = Message.objects.filter(read=False).count()
    slider_images = HomePageSliderImages.objects.all()

    context = {
        "unread_messages": unread_messages,
        "total_unread_messages": total_unread_messages,
        "slider_images": slider_images,
    }
    return render(
        request, "cms/home/slider-images/cms-slider-images.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_add_slider_image(request):
    """
    A view to add a slider image
    """
    context = {}
    form = AddSliderImageForm()
    if request.method == "POST":
        num_of_slider_images = HomePageSliderImages.objects.all().count()
        if num_of_slider_images > 9:
            messages.error(
                request, "You can only have a maximum of 9 slider images")
            return redirect(cp_portfolio)
        form = AddSliderImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Slider image added successfully")
            return redirect(cp_cms_manage_slider_images)
    context["form"] = form
    return render(
        request, "cms/home/slider-images/cms-add-slider-image.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_delete_slider_image_confirm(request, image_id):
    """
    A view to confirm the deletion of a slider image
    """
    context = {}
    image = HomePageSliderImages.objects.get(id=image_id)
    context["image"] = image
    return render(request,
                  "cms/home/slider-images/"
                  "cms-slider-images-confirm-delete.html",
                  context)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_delete_slider_image(request, image_id):
    """
    A view to delete a slider image
    """
    image = HomePageSliderImages.objects.get(id=image_id)
    image.delete()
    messages.success(request, "Carousel image deleted successfully")
    return redirect(cp_cms_manage_slider_images)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_manage_about_section(request):
    unread_messages = Message.objects.filter(read=False)[:5]
    total_unread_messages = Message.objects.filter(read=False).count()

    panels = HomePagePanel.objects.all()

    context = {
        "unread_messages": unread_messages,
        "total_unread_messages": total_unread_messages,
        "panels": panels,
    }
    return render(request, "cms/home/about/cms-about-section.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_add_about_section(request):
    unread_messages = Message.objects.filter(read=False)[:5]
    total_unread_messages = Message.objects.filter(read=False).count()

    context = {
        "unread_messages": unread_messages,
        "total_unread_messages": total_unread_messages,
    }

    form = AddHomePagePanelForm()

    if request.method == "POST":
        form = AddHomePagePanelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Panel added successfully")
            return redirect(cp_cms_manage_about_section)
        else:
            messages.error(request, "There was an error adding the panel")

    context["form"] = form
    return render(request,
                  "cms/home/about/cms-add-about-section.html",
                  context)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_edit_about_section(request, panel_id):
    unread_messages = Message.objects.filter(read=False)[:5]
    total_unread_messages = Message.objects.filter(read=False).count()

    panel = HomePagePanel.objects.get(id=panel_id)
    form = AddHomePagePanelForm(instance=panel)

    if request.method == "POST":
        form = AddHomePagePanelForm(
            request.POST, request.FILES, instance=panel)
        if form.is_valid():
            form.save()
            messages.success(request, "Panel updated successfully")
            return redirect(cp_cms_manage_about_section)
        else:
            messages.error(request, "There was an error updating the panel")

    context = {
        "form": form,
        "unread_messages": unread_messages,
        "total_unread_messages": total_unread_messages,
    }
    return render(request,
                  "cms/home/about/cms-edit-about-section.html",
                  context)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_delete_about_section_confirm(request, panel_id):
    unread_messages = Message.objects.filter(read=False)[:5]
    total_unread_messages = Message.objects.filter(read=False).count()

    panel = HomePagePanel.objects.get(id=panel_id)

    context = {
        "unread_messages": unread_messages,
        "total_unread_messages": total_unread_messages,
        "panel": panel
    }
    return render(request,
                  "cms/home/about/cms-confirm-delete-about-section.html",
                  context)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_delete_about_section(request, panel_id):
    panel = HomePagePanel.objects.get(id=panel_id)
    panel.delete()
    messages.success(request, "Panel deleted successfully")

    return redirect(cp_cms_manage_about_section)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_manage_services(request):
    unread_messages = Message.objects.filter(read=False)[:5]
    total_unread_messages = Message.objects.filter(read=False).count()

    context = {
        "unread_messages": unread_messages,
        "total_unread_messages": total_unread_messages,
    }
    return render(request, "cms/services/services-management.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_edit_services_hero(request):
    unread_messages = Message.objects.filter(read=False)[:5]
    total_unread_messages = Message.objects.filter(read=False).count()

    hero_image = ServicesHero.objects.get(id=1)
    form = ServicesHeroForm(instance=hero_image)

    if request.method == "POST":
        form = ServicesHeroForm(
            request.POST, request.FILES, instance=hero_image)
        if form.is_valid():
            form.save()
            messages.success(request, "Hero image updated successfully")
            return redirect(cp_cms_manage_services)
        else:
            messages.error(
                request, "There was an error updating the hero image")

    context = {
        "form": form,
        "unread_messages": unread_messages,
        "total_unread_messages": total_unread_messages,
    }
    return render(request, "cms/services/cms-edit-hero.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_edit_services_banner(request):
    unread_messages = Message.objects.filter(read=False)[:5]
    total_unread_messages = Message.objects.filter(read=False).count()

    banner = ServicesBanner.objects.get(id=1)
    form = ServicesBannerForm(instance=banner)

    if request.method == "POST":
        form = ServicesBannerForm(request.POST, request.FILES, instance=banner)
        if form.is_valid():
            form.save()
            messages.success(request, "Banner updated successfully")
            return redirect(cp_cms_manage_services)
        else:
            messages.error(request, "There was an error updating the banner")

    context = {
        "form": form,
        "unread_messages": unread_messages,
        "total_unread_messages": total_unread_messages,
    }
    return render(request, "cms/services/cms-edit-banner.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_edit_services_cards(request):
    unread_messages = Message.objects.filter(read=False)[:5]
    total_unread_messages = Message.objects.filter(read=False).count()

    cards = ServicesCards.objects.all()

    context = {
        "unread_messages": unread_messages,
        "total_unread_messages": total_unread_messages,
        "cards": cards,
    }
    return render(request, "cms/services/service-cards.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_edit_services_card(request, card_id):
    unread_messages = Message.objects.filter(read=False)[:5]
    total_unread_messages = Message.objects.filter(read=False).count()

    card = get_object_or_404(ServicesCards, id=card_id)
    form = ServicesCardsForm(instance=card)

    if request.method == "POST":
        form = ServicesCardsForm(request.POST, request.FILES, instance=card)
        if form.is_valid():
            form.save()
            messages.success(request, "Card updated successfully")
            return redirect(cp_cms_edit_services_cards)
        else:
            messages.error(request, "There was an error updating the card")

    context = {
        "form": form,
        "unread_messages": unread_messages,
        "total_unread_messages": total_unread_messages,
        "card": card,
    }
    return render(request, "cms/services/edit-service-card.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_delete_services_card_confirm(request, card_id):
    unread_messages = Message.objects.filter(read=False)[:5]
    total_unread_messages = Message.objects.filter(read=False).count()

    card = ServicesCards.objects.get(id=card_id)

    context = {
        "unread_messages": unread_messages,
        "total_unread_messages": total_unread_messages,
        "card": card,
    }
    return render(request,
                  "cms/services/cms-delete-service-card-confirm.html",
                  context)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_delete_services_card(request, card_id):
    card = ServicesCards.objects.get(id=card_id)
    card.delete()
    messages.success(request, "Card deleted successfully")

    return redirect(cp_cms_edit_services_cards)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_add_services_card(request):
    unread_messages = Message.objects.filter(read=False)[:5]
    total_unread_messages = Message.objects.filter(read=False).count()

    context = {
        "unread_messages": unread_messages,
        "total_unread_messages": total_unread_messages,
    }

    form = ServicesCardsForm()

    if request.method == "POST":
        form = ServicesCardsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Card added successfully")
            return redirect(cp_cms_edit_services_cards)
        else:
            messages.error(request, "There was an error adding the card")

    context["form"] = form
    return render(request,
                  "cms/services/cms-add-service-card.html",
                  context)


"""
Views for user Reviews functionality of CMS
"""


@user_passes_test(lambda u: u.is_superuser)
def cms_manage_reviews(request):
    """
    A view to return the reviews page
    """
    reviews = Review.objects.all()
    context = {
        "reviews": reviews,
    }
    return render(request, "cms/reviews/cms-reviews.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cms_add_review(request):
    """
    A view to add a review
    """
    form = AddReviewForm()
    context = {}
    if request.method == "POST":
        form = AddReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Review added successfully")
            return redirect(cms_manage_reviews)
    context["form"] = form
    return render(request, "cms/reviews/cms-add-review.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cms_delete_review_confirm(request, review_id):
    """
    A view to confirm the deletion of a review
    """
    context = {}
    review = Review.objects.get(id=review_id)
    context["review"] = review
    return render(
        request, "cms/reviews/cms-delete-review-confirm.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cms_delete_review(request, review_id):
    """
    A view to delete a review
    """
    review = Review.objects.get(id=review_id)
    review.delete()
    messages.success(request, "Review deleted successfully")
    return redirect(cms_manage_reviews)


@user_passes_test(lambda u: u.is_superuser)
def cms_edit_review(request, review_id):
    """
    A view to edit a review
    """
    context = {}
    review = get_object_or_404(Review, id=review_id)
    form = AddReviewForm(instance=review)
    context["review"] = review
    if request.method == "POST":
        form = AddReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Review updated successfully")
            return redirect(cms_manage_reviews)
    context["form"] = form
    return render(request, "cms/reviews/cms-edit-review.html", context)


"""
Paths to edit the context banners for the services page
"""


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_edit_context_banner_one(request):
    unread_messages = Message.objects.filter(read=False)[:5]
    total_unread_messages = Message.objects.filter(read=False).count()

    banner = ServicesContextBannerOne.objects.get(id=1)
    form = ServicesBannerForm(instance=banner)

    if request.method == "POST":
        form = ServicesBannerForm(request.POST, request.FILES, instance=banner)
        if form.is_valid():
            form.save()
            messages.success(request, "Banner updated successfully")
            return redirect(cp_cms_manage_services)
        else:
            messages.error(request, "There was an error updating the banner")

    context = {
        "form": form,
        "unread_messages": unread_messages,
        "total_unread_messages": total_unread_messages,
    }
    return render(request, "cms/services/cms-edit-context-banner-one.html",
                  context)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_edit_context_banner_two(request):
    unread_messages = Message.objects.filter(read=False)[:5]
    total_unread_messages = Message.objects.filter(read=False).count()

    banner = ServicesContextBannerTwo.objects.get(id=1)
    form = ServicesBannerForm(instance=banner)

    if request.method == "POST":
        form = ServicesBannerForm(request.POST, request.FILES, instance=banner)
        if form.is_valid():
            form.save()
            messages.success(request, "Banner updated successfully")
            return redirect(cp_cms_manage_services)
        else:
            messages.error(request, "There was an error updating the banner")

    context = {
        "form": form,
        "unread_messages": unread_messages,
        "total_unread_messages": total_unread_messages,
    }
    return render(request, "cms/services/cms-edit-context-banner-two.html",
                  context)