from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from home.models import (
  Message,
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

    form = HomePageFAQForm()

    if request.method == "POST":
        form = HomePageFAQForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "FAQ added successfully")
            return redirect(cp_cms_faq)
        
    context = {
        "form": form,
        "unread_messages": unread_messages,
        "total_unread_messages": total_unread_messages,
        "page_title": "Add FAQ",
        "end_point": "cms_add_faq",
    }
    return render(request, "generic/add-item.html", context)


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
