from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
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
      return HttpResponse(
        content=f'Webhook received: {event["type"]}',
        status=200
      )
      
  def handle_payment_intent_payment_failed(self, event):
      """Handle the payment_intent.failed webhook from Stripe"""
      return HttpResponse(
        content=f'Webhook received: {event["type"]}',
        status=200
      )