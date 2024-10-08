from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404, reverse

from home.models import Message
from portfolio.models import PortfolioImages

from controlpanel.forms import AddPortfolioImage


@user_passes_test(lambda u: u.is_superuser)
def cp_portfolio(request):
    """
    A view to return the portfolio page
    """
    
    total_unread_messages = Message.objects.filter(read=False).count()
    unread_messages = Message.objects.filter(read=False)[:5]
    portfolio_images = PortfolioImages.objects.all()
    
    context = {
        "portfolio_images": portfolio_images,
        "total_unread_messages": total_unread_messages,
        "unread_messages": unread_messages
    }
    return render(request, "portfolio/portfolio-management.html", context)


@user_passes_test(lambda u: u.is_superuser)
def add_portfolio_image(request):
    """
    A view to add a slider image
    """
    total_unread_messages = Message.objects.filter(read=False).count()
    unread_messages = Message.objects.filter(read=False)[:5]

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
        "total_unread_messages": total_unread_messages,
        "unread_messages": unread_messages
    }
    return render(request, "generic/add-item.html", context)


@user_passes_test(lambda u: u.is_superuser)
def delete_portfolio_image_confirm(request, image_id):
    """
    A view to confirm the deletion of a portfolio image
    """
    image = get_object_or_404(PortfolioImages, id=image_id)
    total_unread_messages = Message.objects.filter(read=False).count()
    unread_messages = Message.objects.filter(read=False)[:5]

    context = {
        "image": image,
        "total_unread_messages": total_unread_messages,
        "unread_messages": unread_messages
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