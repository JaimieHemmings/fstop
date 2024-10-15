from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404
from home.models import AboutPage
from home.forms import AboutPageForm

@user_passes_test(lambda u: u.is_superuser)
def cp_cms_about_edit(request):
    page_info = get_object_or_404(AboutPage, title="About")
    form = AboutPageForm(instance=page_info)

    if request.method == "POST":
        form = AboutPageForm(request.POST, request.FILES, instance=page_info)
        if form.is_valid():
            form.save()

    context = {
        "form": form,
        "page_info": page_info,
        "end_point": "cp_cms_about_edit",
    }

    return render(request, "cms/about/edit-about.html", context)
