from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404, reverse
from home.models import Message

from payments.models import Payment

from controlpanel.forms import NewPaymentForm


@user_passes_test(lambda u: u.is_superuser)
def cp_payments(request):
    """
    A view to return the payments page
    """
    total_unread_messages = Message.objects.filter(read=False).count()
    unread_messages = Message.objects.filter(read=False)[:5]
    payments = Payment.objects.all()

    context = {
        "payments": payments,
        "total_unread_messages": total_unread_messages,
        "unread_messages": unread_messages,
    }
    return render(request, "payments/payment-management.html", context)


@user_passes_test(lambda u: u.is_superuser)
def new_payment(request):
    """
    A view to add a payment
    """
    total_unread_messages = Message.objects.filter(read=False).count()
    unread_messages = Message.objects.filter(read=False)[:5]
    form = NewPaymentForm()

    if request.method == "POST":
        form = NewPaymentForm(request.POST)
        if form.is_valid():
            # Use the email address to get the users name
            email = form.cleaned_data["email"]
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                messages.error(
                    request, "No user found with that email address")
                context = {
                    "form": form,
                }
                return render(request, "payments/new-payment.html", context)
            name = user.first_name + " " + user.last_name
            form.instance.name = name
            form.save()
            messages.success(request, "Payment request added successfully")
            return redirect(reverse("cp_payments"))
    context = {
        "form": form,
        "page_title": "Add Payment Request",
        "end_point": "new_payment",
        "unread_messages": unread_messages,
        "total_unread_messages": total_unread_messages,
    }
    return render(request, "generic/add-item.html", context)


@user_passes_test(lambda u: u.is_superuser)
def view_payment(request, payment_id):
    """
    A view to view the details of a payment
    """
    total_unread_messages = Message.objects.filter(read=False).count()
    unread_messages = Message.objects.filter(read=False)[:5]
    payment = get_object_or_404(Payment, id=payment_id)
    context = {
        "payment": payment,
        "unread_messages": unread_messages,
        "total_unread_messages": total_unread_messages,
    }
    return render(request, "payments/view-payment.html", context)

