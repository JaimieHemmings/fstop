from django.urls import path
from . import views

urlpatterns = [
  path('', views.control_panel, name='control_panel'),
  path('articles/', views.cp_articles, name='cp_articles'),
  path('messages/', views.cp_messages, name='cp_messages'),
  path('messages/toggle-read/<int:message_id>/', views.toggle_read, name='toggle_read'),
  path(
    'messages/confirm-delete-message/<int:message_id>/',
    views.delete_message_confirm,
    name='delete_message_confirm'),
    path('messages/delete-message/<int:message_id>/', views.delete_message, name='delete_message'),
]