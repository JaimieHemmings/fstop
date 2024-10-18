from django.contrib import admin
from .models import Payment


class PaymentAdmin(admin.ModelAdmin):
    readonly_fields = (
        "payment_id", "date", "paid", "paid_date",
        "amount", "stripe_id",
    )

    fields = (
        "payment_id", "full_name", "email", "phone_number", "date",
        "street_address1", "street_address2",
        "town_or_city", "county", "country", "postcode", "amount",
        "paid", "paid_date", "stripe_id", "description",
    )

    list_display = (
        "payment_id", "full_name", "email", "phone_number",
        "date", "amount", "paid", "paid_date",
    )

    ordering = ("-date",)


admin.site.register(Payment, PaymentAdmin)
