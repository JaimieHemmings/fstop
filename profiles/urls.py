from django.urls import path
from . import views
from webhooks.py import webhook

urlpatterns = [
    path("", views.profile, name="profile"),
    path("edit-profile/", views.edit_profile, name="edit_profile"),
    path("make-payment/<int:id>", views.make_payment, name="make_payment"),
    path("payment-success/<int:id>", views.payment_success, name="payment_success"),
    path("wh/", webhook, name="webhook"),
]
