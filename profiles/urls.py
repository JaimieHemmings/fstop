from django.urls import path
from . import views
#from webhooks import webhook

urlpatterns = [
    path("", views.profile_page, name="profile_page"),
    path("make-payment/<int:id>", views.make_payment, name="make_payment"),
    path("payment-success/<int:id>", views.payment_success, name="payment_success"),
    #path("wh/", webhook, name="webhook"),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
]
