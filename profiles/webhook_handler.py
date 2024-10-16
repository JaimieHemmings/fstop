from django.http import HttpResponse
from payments.models import Payment

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
      amount = intent.amount / 100
      billing_details = intent.charges.data[0].billing_details
      # Clean the data in the billing details
      for field, value in billing_details.address.items():
          if value == "":
              billing_details.address[field] = None
      # Attempt to find the order
      try:
        payment = Payment.objects.get(
            full_name__iexact=billing_details.name,
            email__iexact=billing_details.email,
            phone_number__iexact=billing_details.phone,
            amount=amount,
        )
        payment.paid = True
        payment.stripe_id = pid
        payment.save()
        return HttpResponse(
          content=f'Webhook received: {event["type"]} | SUCCESS: Updated order status',
          status=200
        )
      except Exception as e:
        return HttpResponse(
          content=f'Webhook received: {event["type"]} | ERROR: {e}',
          status=500
        )

      
  def handle_payment_intent_payment_failed(self, event):
      """Handle the payment_intent.failed webhook from Stripe"""
      return HttpResponse(
        content=f'Webhook received: {event["type"]}',
        status=200
      )