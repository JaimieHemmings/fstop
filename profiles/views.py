from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from payments.models import Payment
from .forms import UserProfileForm
from .models import UserProfile
from payments.models import Payment
from django.contrib import messages
import stripe


@login_required
def profile(request):
    """
    View to display the user's profile
    """
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    payments = Payment.objects.filter(email=user.email)
    context = {"user": user, "payments": payments, "user_profile": user_profile}
    return render(request, "profile.html", context)


@login_required
def edit_profile(request):
    """
    View to edit the user's profile
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(instance=profile)
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return render(request, "profile.html", {"user": request.user})
        else:
            form = UserProfileForm(instance=profile)
    context = {
        "form": form,
    }
    return render(request, "edit-profile.html", context)


@login_required
def make_payment(request, id):
    """
    View to make a payment
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY


    order = get_object_or_404(Payment, pk=id)
    user_profile = UserProfile.objects.get(user=request.user)
    context = {"order": order, "user_profile": user_profile}

    full_name = user_profile.fname + " " + user_profile.lname

    total = order.amount
    stripe_total = round(total * 100)

    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        customer = full_name,
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if not stripe_public_key:
        messages.warning(
            request,
            "Stripe public key is missing. Did you forget to set it in your environment?",
        )

    context = {
        # add form
        "stripe_public_key": stripe_public_key,
        "client_secret": intent.client_secret,
    }

    return render(request, "make-payment.html", context)
