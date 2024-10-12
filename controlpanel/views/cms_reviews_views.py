from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404, reverse

from reviews.models import Review

from controlpanel.forms import AddReviewForm


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

    if request.method == "POST":
        form = AddReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Review added successfully")
            return redirect(cms_manage_reviews)

    context = {
        "form": form,
    }

    return render(request, "cms/reviews/cms-add-review.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cms_delete_review_confirm(request, review_id):
    """
    A view to confirm the deletion of a review
    """
    review = get_object_or_404(Review, id=review_id)

    context = {
        "review": review,
    }

    return render(
        request, "cms/reviews/cms-delete-review-confirm.html", context)


@user_passes_test(lambda u: u.is_superuser)
def cms_delete_review(request, review_id):
    """
    A view to delete a review
    """
    review = get_object_or_404(Review, id=review_id)
    review.delete()
    messages.success(request, "Review deleted successfully")
    return redirect(reverse("cms_manage_reviews"))


@user_passes_test(lambda u: u.is_superuser)
def cms_edit_review(request, review_id):
    """
    A view to edit a review
    """
    review = get_object_or_404(Review, id=review_id)
    form = AddReviewForm(instance=review)

    if request.method == "POST":
        form = AddReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Review updated successfully")
            return redirect(reverse("cms_manage_reviews"))

    context = {
        "form": form,
        "review": review,
    }

    return render(request, "cms/reviews/cms-edit-review.html", context)
