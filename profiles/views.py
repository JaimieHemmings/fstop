from django.conf import settings
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST

from payments.models import Payment
from payments.forms import PaymentForm

from .forms import UserProfileForm
from .models import UserProfile

# from payments.forms import PaymentForm
import stripe


@login_required
def profile(request):
    """
    View to display the user's profile
    """
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    payments = Payment.objects.filter(email=user.email)
    context = {
        "user": user,
        "payments": payments,
        "user_profile": user_profile
        }
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
            return render(
                request, "profile.html", {"user": request.user})
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

    if request.method == "POST":

        form_data = {
            
        }

        form = PaymentForm(form_data)
        if form.is_valid():
            form.save()
            stripe_payment_id = 0
            return render(
                request, "payment-success.html", stripe_payment_id)
        else:
            messages.error(
                request, "Failed to make payment."
                "Please ensure the form is valid.")

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
            "Stripe public key is missing."
            "Did you forget to set it in your environment?",
        )

    context = {
        # add form
        "stripe_public_key": stripe_public_key,
        "client_secret": intent.client_secret,
    }

    return render(request, "make-payment.html", context)


@require_POST
def cache_checkout_data(request):
    """
    View to cache checkout data
    """
    try:
        pid = request.POST.get("client_secret").split("_secret")[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.paymentIntent.modify(pid, metadata={
            "username": request.user,
            "save_info": request.POST.get("save_info"),
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(
            request,
            "Sorry, your payment cannot be processed right now."
                       "Please try again later.")
        return HttpResponse(content=e, status=400)


@login_required
def payment_success(request, stripe_payment_id):
    """
    View to display payment success
    """
    payment = get_object_or_404(Payment, stripe_payment_id=stripe_payment_id)
    context = {"payment": payment}
    messages.success(
        request, f"Payment success!"
        "We will send a confirmation email to {payment.email}")
    return render(request, "payment-success.html", context)
