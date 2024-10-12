from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, reverse


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_manage_services(request):
    return render(request, "cms/services/services-management.html")


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_edit_services_hero(request):
    return render(request, "cms/services/cms-edit-hero.html")


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_edit_services_banner(request):
    return render(request, "cms/services/cms-edit-banner.html")


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_edit_services_cards(request):
    return render(request, "cms/services/service-cards.html")


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_edit_services_card(request, card_id):
    return render(request, "cms/services/edit-service-card.html")


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_delete_services_card_confirm(request, card_id):
    return render(request,
                  "cms/services/cms-delete-service-card-confirm.html",)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_delete_services_card(request, card_id):
    messages.success(request, "Card deleted successfully")
    return redirect(reverse("cp_cms_edit_services_cards"))


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_add_services_card(request):
    return render(request,
                  "cms/services/cms-add-service-card.html")

"""
Paths to edit the context banners for the services page
"""


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_edit_context_banner_one(request):
    return render(request,
                  "cms/services/cms-edit-context-banner-one.html")


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_edit_context_banner_two(request):
    return render(request,
                  "cms/services/cms-edit-context-banner-two.html")