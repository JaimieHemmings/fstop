from django.conf import settings
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.shortcuts import redirect

from payments.models import Payment
from payments.forms import PaymentForm

from .forms import UserProfileForm
from .models import UserProfile

# from payments.forms import PaymentForm
import stripe


@login_required
def profile_page(request):
    """
    View to display the user's profile and allow editing
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    payments = Payment.objects.filter(email=request.user.email)
    form = UserProfileForm(instance=profile)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
            return redirect(profile_page)
        else:
            form = UserProfileForm(instance=profile)
            messages.error(
                request, "Failed to update profile."
                "Please ensure the form is valid.")

    context = {
        "profile": profile,
        "payments": payments,
        "form": form,
        }
    
    return render(request, "profile.html", context)


@login_required
def make_payment(request, id):
    """
    View to make a payment
    """
    payment_data = get_object_or_404(Payment, id=id)

    profile = get_object_or_404(UserProfile, user=request.user)
    form = PaymentForm(initial={
        "full_name": profile.fname + " " + profile.lname,
        "email": request.user.email,
        "country": profile.country,
        "postcode": profile.postcode,
        "town_or_city": profile.town_or_city,
        "street_address1": profile.street_address1,
        "street_address2": profile.street_address2,
        "county": profile.county,
        "save_info": True,
    })

    if settings.DEBUG:
        STRIPE_PUBLIC_KEY = "generic_key"
    else:
        STRIPE_PUBLIC_KEY = settings.STRIPE_PUBLIC_KEY

        
    payment_amount_stripe = int(payment_data.amount * 100)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    payment_intent = stripe.PaymentIntent.create(
        amount=payment_amount_stripe,
        currency=settings.STRIPE_CURRENCY,
        description=payment_data.description,
    )

    if request.method == "POST":
        if form.is_valid():
            form.save()
            payment_data = Payment.objects.get(id=id)
            payment_data.paid = True
            return render(
                request, "payment-success.html", payment_data.payment_id)
        else:
            messages.error(
                request, "Failed to make payment."
                "Please ensure the form is valid.")
    context = {
        "form": form,
        "payment_data": payment_data,
        "stripe_public_key": STRIPE_PUBLIC_KEY,
        "client_secret": payment_intent.client_secret,
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
            "username": request.user
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
