from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
]