from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404, reverse

from home.models import Message
from services.models import (
    ServicesHero,
    ServicesBanner,
    ServicesCards,
    ServicesContextBannerOne,
    ServicesContextBannerTwo,
)

from services.forms import (
  ServicesHeroForm,
  ServicesBannerForm,
  ServicesCardsForm,
)


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
            return redirect(reverse("cp_cms_manage_services"))
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
            return redirect(reverse("cp_cms_manage_services"))
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
            return redirect(reverse("cp_cms_edit_services_cards"))
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

    card = get_object_or_404(ServicesCards, id=card_id)

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
    card = get_object_or_404(ServicesCards, id=card_id)
    card.delete()
    messages.success(request, "Card deleted successfully")

    return redirect(reverse("cp_cms_edit_services_cards"))


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
            return redirect(reverse("cp_cms_edit_services_cards"))
        else:
            messages.error(request, "There was an error adding the card")

    context["form"] = form
    return render(request,
                  "cms/services/cms-add-service-card.html",
                  context)

"""
Paths to edit the context banners for the services page
"""


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_edit_context_banner_one(request):
    unread_messages = Message.objects.filter(read=False)[:5]
    total_unread_messages = Message.objects.filter(read=False).count()

    banner = get_object_or_404(ServicesContextBannerOne, id=1)
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

    banner = get_object_or_404(ServicesContextBannerTwo, id=1)
    form = ServicesBannerForm(instance=banner)

    if request.method == "POST":
        form = ServicesBannerForm(request.POST, request.FILES, instance=banner)
        if form.is_valid():
            form.save()
            messages.success(request, "Banner updated successfully")
            return redirect(reverse("cp_cms_manage_services"))
        else:
            messages.error(request, "There was an error updating the banner")

    context = {
        "form": form,
        "unread_messages": unread_messages,
        "total_unread_messages": total_unread_messages,
    }
    return render(request, "cms/services/cms-edit-context-banner-two.html",
                  context)