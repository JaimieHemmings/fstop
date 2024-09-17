from django.urls import path
from . import views

urlpatterns = [
  path('', views.control_panel, name='control_panel'),
  path('articles/', views.cp_articles, name='cp_articles'),
  path('messages/', views.cp_messages, name='cp_messages'),
  path('messages/toggle_read/<int:message_id>/', views.toggle_read, name='toggle_read'),
]