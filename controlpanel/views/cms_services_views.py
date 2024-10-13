from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404
from service.models import ServicesPage
from service.forms import EditServicesPageForm
from django.contrib import messages


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_manage_services(request):
    return render(request, "cms/services/services-management.html")


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_edit_lifestyle(request):
    page_info = get_object_or_404(ServicesPage, title="Lifestyle")
    form = EditServicesPageForm(instance=page_info)

    if request.method == "POST":
        form = EditServicesPageForm(
            request.POST, request.FILES, instance=page_info)
        if form.is_valid():
            form.save()
            messages.success(request, "Page data updated successfully")
            

    context = {
        "form": form,
        "page_info": page_info,
        "end_point": "cp_cms_edit_lifestyle",
    }

    return render(request, "cms/services/edit-page.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_edit_event(request):
    page_info = get_object_or_404(ServicesPage, title="Event")
    form = EditServicesPageForm(instance=page_info)

    if request.method == "POST":
        form = EditServicesPageForm(
            request.POST, request.FILES, instance=page_info)
        if form.is_valid():
            form.save()
            messages.success(request, "Page data updated successfully")

    context = {
        "form": form,
        "page_info": page_info,
        "end_point": "cp_cms_edit_event",
    }

    return render(request, "cms/services/edit-page.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_edit_property(request):
    page_info = get_object_or_404(ServicesPage, title="Property")
    form = EditServicesPageForm(instance=page_info)

    if request.method == "POST":
        form = EditServicesPageForm(
            request.POST, request.FILES, instance=page_info)
        if form.is_valid():
            form.save()
            messages.success(request, "Page data updated successfully")

    context = {
        "form": form,
        "page_info": page_info,
        "end_point": "cp_cms_edit_property",
    }

    return render(request, "cms/services/edit-page.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cp_cms_edit_aerial(request):
    page_info = get_object_or_404(ServicesPage, title="Aerial")
    form = EditServicesPageForm(instance=page_info)

    if request.method == "POST":
        form = EditServicesPageForm(
            request.POST, request.FILES, instance=page_info)
        if form.is_valid():
            form.save()
            messages.success(request, "Page data updated successfully")

    context = {
        "form": form,
        "page_info": page_info,
        "end_point": "cp_cms_edit_aerial",
    }

    return render(request, "cms/services/edit-page.html", context)
    