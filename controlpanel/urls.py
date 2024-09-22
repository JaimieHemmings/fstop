from django.urls import path
from . import views

urlpatterns = [
  path(
    '',
    views.control_panel,
    name='control_panel'),

  # Article Management URL's
  path(
    'articles/',
    views.cp_articles,
    name='cp_articles'),
  path(
    'articles/create-new/',
    views.add_article,
    name='add_article'),
  path(
    'articles/edit-article/<int:article_id>/',
    views.edit_article,
    name='edit_article'),
  path(
    'articles/delete-article/<int:article_id>/',
    views.delete_article_confirm,
    name='confirm_delete_article'),
  path(
    'articles/delete-article/<int:article_id>/confirmed/',
    views.delete_article,
    name='delete_article'),

  # Message Management URL's
  path(
    'messages/',
    views.cp_messages,
    name='cp_messages'),
  path(
    'messages/toggle-read/<int:message_id>/',
    views.toggle_read,
    name='toggle_read'),
  path(
    'messages/confirm-delete-message/<int:message_id>/',
    views.delete_message_confirm,
    name='delete_message_confirm'),
  path(
    'messages/delete-message/<int:message_id>/',
    views.delete_message,
    name='delete_message'),

  # Portfolio Management URL's
  path(
    'portfolio/',
    views.cp_portfolio,
    name='cp_portfolio'),
  path(
    'portfolio/add-slider-image/',
    views.add_slider_image,
    name='add_slider_image'),
  path(
    'portfolio/add-portfolio-image/',
    views.add_portfolio_image,
    name='add_portfolio_image'),
    path(
      'portfolio/delete-slider-image/<int:image_id>/',
      views.delete_slider_image_confirm,
      name='delete_slider_image_confirm'
    ),
    path(
      'portfolio/delete-portfolio-image/<int:image_id>/',
      views.delete_portfolio_image_confirm,
      name='delete_portfolio_image_confirm'
    ),
    path(
      'portfolio/delete-slider-image/<int:image_id>/confirmed/',
      views.delete_slider_image,
      name='delete_slider_image'
    ),
    path(
      'portfolio/delete-portfolio-image/<int:image_id>/confirmed/',
      views.delete_portfolio_image,
      name='delete_portfolio_image'
    ),

    # Review Management URL's
    path(
      'manage-reviews/',
      views.manage_reviews,
      name='manage_reviews'
    ),
    path(
      'manage-reviews/add-review/',
      views.add_review,
      name='add_review'
    ),
    path(
      'manage-reviews/delete-review/<int:review_id>/',
      views.delete_review_confirm,
      name='delete_review_confirm'
    ),
    path(
      'manage-reviews/delete-review/<int:review_id>/confirmed/',
      views.delete_review,
      name='delete_review'
    ),
    path(
      'manage-reviews/edit-review/<int:review_id>/',
      views.edit_review,
      name='edit_review'
    ),

    # Payment Management URL's
    path(
      'manage-payments/',
      views.cp_payments,
      name='cp_payments'
    ),
    path(
      'manage-payments/new-payment/',
      views.new_payment,
      name='new_payment'
    ),
    path(
      'manage-payments/view-details/<int:payment_id>/',
      views.view_payment,
      name='view_payment'
    ),
]
