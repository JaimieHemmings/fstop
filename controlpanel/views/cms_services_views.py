from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404, reverse

from home.models import Message


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

    context = {
        "unread_messages": unread_messages,
        "total_unread_messages": total_unread_messages,
    }
    return render(request, "cms/services/cms-edit-hero.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_edit_services_banner(request):
    unread_messages = Message.objects.filter(read=False)[:5]
    total_unread_messages = Message.objects.filter(read=False).count()

    context = {
        "unread_messages": unread_messages,
        "total_unread_messages": total_unread_messages,
    }
    return render(request, "cms/services/cms-edit-banner.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_edit_services_cards(request):
    unread_messages = Message.objects.filter(read=False)[:5]
    total_unread_messages = Message.objects.filter(read=False).count()

    context = {
        "unread_messages": unread_messages,
        "total_unread_messages": total_unread_messages,
    }
    return render(request, "cms/services/service-cards.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_edit_services_card(request, card_id):
    unread_messages = Message.objects.filter(read=False)[:5]
    total_unread_messages = Message.objects.filter(read=False).count()

    context = {
        "unread_messages": unread_messages,
        "total_unread_messages": total_unread_messages,
    }
    return render(request, "cms/services/edit-service-card.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_delete_services_card_confirm(request, card_id):
    unread_messages = Message.objects.filter(read=False)[:5]
    total_unread_messages = Message.objects.filter(read=False).count()

    context = {
        "unread_messages": unread_messages,
        "total_unread_messages": total_unread_messages,
    }
    return render(request,
                  "cms/services/cms-delete-service-card-confirm.html",
                  context)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_delete_services_card(request, card_id):
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

    context = {
        "unread_messages": unread_messages,
        "total_unread_messages": total_unread_messages,
    }
    return render(request,
                  "cms/services/cms-edit-context-banner-one.html",
                  context)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_edit_context_banner_two(request):
    unread_messages = Message.objects.filter(read=False)[:5]
    total_unread_messages = Message.objects.filter(read=False).count()

    context = {
        "unread_messages": unread_messages,
        "total_unread_messages": total_unread_messages,
    }

    return render(request,
                  "cms/services/cms-edit-context-banner-two.html",
                  context)