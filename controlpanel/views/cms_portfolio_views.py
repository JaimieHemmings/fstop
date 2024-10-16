from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404, reverse

from portfolio.models import PortfolioImages

from controlpanel.forms import AddPortfolioImage


@user_passes_test(lambda u: u.is_superuser)
def cp_portfolio(request):
    """
    A view to return the portfolio page
    """
    portfolio_images = PortfolioImages.objects.all()

    context = {
        "portfolio_images": portfolio_images,
    }
    return render(request, "portfolio/portfolio-management.html", context)


@user_passes_test(lambda u: u.is_superuser)
def add_portfolio_image(request):
    """
    A view to add a slider image
    """

    form = AddPortfolioImage()
    if request.method == "POST":
        form = AddPortfolioImage(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Portfolio image added successfully")
            return redirect(reverse("cp_portfolio"))

    context = {
        "form": form,
        "page_title": "Add Portfolio Image",
        "end_point": "add_portfolio_image",
    }
    return render(request, "generic/add-item.html", context)


@user_passes_test(lambda u: u.is_superuser)
def delete_portfolio_image_confirm(request, image_id):
    """
    A view to confirm the deletion of a portfolio image
    """
    image = get_object_or_404(PortfolioImages, id=image_id)

    context = {
        "image": image,
    }

    return render(
        request, "portfolio/delete-portfolio-image-confirm.html", context)


@user_passes_test(lambda u: u.is_superuser)
def delete_portfolio_image(request, image_id):
    """
    A view to delete a portfolio image
    """
    image = get_object_or_404(PortfolioImages, id=image_id)

    image.delete()
    messages.success(request, "Portfolio image deleted successfully")
    return redirect(reverse("cp_portfolio"))
