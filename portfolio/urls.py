from django.urls import path
from . import views

urlpatterns = [
    path("", views.portfolio, name="portfolio"),
    # path('<int:blog_id>/', views.detail, name='detail'),
]
