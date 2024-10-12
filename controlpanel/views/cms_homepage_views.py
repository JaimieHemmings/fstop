from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from home.models import (
  HomePageHero,
  HomePageAbout,
  HomePageTrustedBy,
  HomePageFAQ,
  HomePagePanel
)
from home.models import HomePageSliderImages

from home.forms import AddSliderImageForm
from home.forms import (
  HomeHeroForm,
  editAboutSectionHomeForm,
  HomePageTrustedByForm,
  HomePageFAQForm,
  AddHomePagePanelForm
)

@user_passes_test(lambda u: u.is_superuser)
def cp_cms_home(request):
    """
    A view to return the CMS homepage
    """
    return render(request, "cms/cms-homepage.html")


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_hero(request):
    """
    A view to return the CMS homepage
    """
    home_hero_data = get_object_or_404(HomePageHero, id=1)
    form = HomeHeroForm(instance=home_hero_data)

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
    }

    return render(request, "cms/home/cms-edit-hero.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_about_home_edit(request):
    """
    A view to return the CMS homepage about page
    """
    about_data = get_object_or_404(HomePageAbout, id=1)
    form = editAboutSectionHomeForm(instance=about_data)

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
    }

    return render(request, "cms/home/cms-edit-about-home.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_trusted_by_edit(request):
    """
    A view to return the CMS homepage about page
    """
    trusted_by_data = get_object_or_404(HomePageTrustedBy, id=1)
    form = HomePageTrustedByForm(instance=trusted_by_data)

    context = {
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
    faqs = HomePageFAQ.objects.all()
    context = {
        "faqs": faqs,
    }
    return render(request, "cms/faqs/cms-faqs.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cms_add_faq(request):
    """
    A view to add a FAQ
    """
    form = HomePageFAQForm()

    if request.method == "POST":
        form = HomePageFAQForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "FAQ added successfully")
            return redirect(reverse("cp_cms_faq"))
        
    context = {
        "form": form,
        "page_title": "Add FAQ",
        "end_point": "cms_add_faq",
    }
    return render(request, "generic/add-item.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cms_edit_faq(request, faq_id):
    """
    A view to edit a FAQ
    """
    context = {
    }
    faq = get_object_or_404(HomePageFAQ, id=faq_id)
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

    faq = get_object_or_404(HomePageFAQ, id=faq_id)

    context = {
        "faq": faq,
    }
    return render(request, "cms/faqs/cms-faq-confirm-delete.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cms_delete_faq(request, faq_id):
    """
    A view to delete a FAQ
    """
    faq = get_object_or_404(HomePageFAQ, id=faq_id)
    faq.delete()
    messages.success(request, "FAQ deleted successfully")
    return redirect(reverse("cp_cms_faq"))


"""
Homepage Slider Images Management
"""


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_manage_slider_images(request):
    """
    A view to return the CMS homepage slider images page
    """
    slider_images = HomePageSliderImages.objects.all()

    context = {
        "slider_images": slider_images,
    }
    return render(
        request, "cms/home/slider-images/cms-slider-images.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_add_slider_image(request):
    """
    A view to add a slider image
    """
    form = AddSliderImageForm()
    if request.method == "POST":
        num_of_slider_images = HomePageSliderImages.objects.all().count()
        if num_of_slider_images > 9:
            messages.error(
                request, "You can only have a maximum of 9 slider images")
            return redirect(cp_cms_manage_slider_images)
        form = AddSliderImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Slider image added successfully")
            return redirect(cp_cms_manage_slider_images)
    
    context = {
        "form": form,
        "page_title": "Add Slider Image",
        "end_point": "cp_cms_add_slider_image",
    }

    return render(
        request, "generic/add-item.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_delete_slider_image_confirm(request, image_id):
    """
    A view to confirm the deletion of a slider image
    """
    context = {}
    image = get_object_or_404(HomePageSliderImages, id=image_id)
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
    image = get_object_or_404(HomePageSliderImages, id=image_id)
    image.delete()
    messages.success(request, "Carousel image deleted successfully")
    return redirect(reverse("cp_cms_manage_slider_images"))


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_manage_about_section(request):

    panels = HomePagePanel.objects.all()

    context = {
        "panels": panels,
    }
    return render(request, "cms/home/about/cms-about-section.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_add_about_section(request):

    context = {
    }

    form = AddHomePagePanelForm()

    if request.method == "POST":
        form = AddHomePagePanelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Panel added successfully")
            return redirect(reverse("cp_cms_manage_about_section"))
        else:
            messages.error(request, "There was an error adding the panel")

    context["form"] = form
    return render(request,
                  "cms/home/about/cms-add-about-section.html",
                  context)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_edit_about_section(request, panel_id):

    panel = get_object_or_404(HomePagePanel, id=panel_id)
    form = AddHomePagePanelForm(instance=panel)

    if request.method == "POST":
        form = AddHomePagePanelForm(
            request.POST, request.FILES, instance=panel)
        if form.is_valid():
            form.save()
            messages.success(request, "Panel updated successfully")
            return redirect(reverse("cp_cms_manage_about_section"))
        else:
            messages.error(request, "There was an error updating the panel")

    context = {
        "form": form,
    }
    return render(request,
                  "cms/home/about/cms-edit-about-section.html",
                  context)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_delete_about_section_confirm(request, panel_id):

    panel = get_object_or_404(HomePagePanel, id=panel_id)

    context = {
        "panel": panel
    }
    return render(request,
                  "cms/home/about/cms-confirm-delete-about-section.html",
                  context)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_delete_about_section(request, panel_id):
    panel = get_object_or_404(HomePagePanel, id=panel_id)
    panel.delete()
    messages.success(request, "Panel deleted successfully")

    return redirect(reverse("cp_cms_manage_about_section"))
