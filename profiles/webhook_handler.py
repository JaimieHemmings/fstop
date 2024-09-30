from django.http import HttpResponse
import stripe
import time

class stripeWH_Handler:
  """Handle Stripe Webhooks"""

  def __init__(self, request):
    self.request = request

    def handle_event(self, event):
      """Handle a generic/unknown/unexpected webhook event"""
      return HttpResponse(
        content=f'Unhandled Webhook received: {event["type"]}',
        status=200
      )
    
    def handle_payment_intent_succeeded(self, event):
      """Handle the payment_intent.succeeded webhook from Stripe"""
      intent = event.data.object
      pid = intent.id
      save_info = intent.metadata.save_info

      stripe_charge = stripe.Charge.retrieve(
        intent.latest_charge
      )

      billing_details = stripe_charge.billing_details
      shipping_details = intent.shipping

      grand_total = round(intent.charges.data[0].amount / 100, 2)

      # Clean data in the shipping details
      for field, value in shipping_details.address.items():
        if value == "":
          shipping_details.address[field] = None

      order_exists = False
      attempt = 1
      while attempt <= 5:
        try:
          order = Order.objects.get(
            full_name__iexact=shipping_details.name,
            email__iexact=shipping_details.email,
            phone_number__iexact=shipping_details.phone,
            country__iexact=shipping_details.address.country,
            street_address1__iexact=shipping_details.address.line1,
            street_address2__iexact=shipping_details.address.line2,
            town_or_city__iexact=shipping_details.address.city,
            county__iexact=shipping_details.address.state,
            postcode__iexact=shipping_details.address.postal_code,
            grand_total=grand_total,
            stripe_pid=pid,
          )
          order_exists = True
          break
        except Order.DoesNotExist:
          attempt += 1
          time.sleep(1)
      if order_exists:
        return HttpResponse(
          content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
          status=200
        )
      else:
          order = None
          try:
            order = Order.objects.create(
              full_name=shipping_details.name,
              email=shipping_details.email,
              phone_number=shipping_details.phone,
              country=shipping_details.address.country,
              street_address1=shipping_details.address.line1,
              street_address2=shipping_details.address.line2,
              town_or_city=shipping_details.address.city,
              county=shipping_details.address.state,
              postcode=shipping_details.address.postal_code,
              grand_total=grand_total,
              stripe_pid=pid,
            )
          except Exception as e:
            if order:
                order.delete()
            return HttpResponse(
              content=f'Webhook received: {event["type"]} | ERROR: {e}',
              status=500
            )   

      return HttpResponse(
        content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
        status=200
      )
    
    def handle_payment_intent_failed(self, event):
      """Handle the payment_intent.failed webhook from Stripe"""
      return HttpResponse(
        content=f'Webhook received: {event["type"]}',
        status=200
      )
