from django.urls import path
from . import views

urlpatterns = [
  path("", views.services, name="services"),
  path("lifestyle/", views.lifestyle_services, name="lifestyle_services"),
  path("event/", views.event_services, name="event_services"),
  path("property/", views.property_services, name="property_services"),
  path("aerial/", views.aerial_services, name="aerial_services"),
]
