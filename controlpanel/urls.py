from django.urls import path
from . import views

urlpatterns = [
    # Control Panel Root
    path("", views.control_panel, name="control_panel"),

    # Article Management URL's
    path("articles/", views.cp_articles, name="cp_articles"),
    path("articles/create-new/", views.add_article, name="add_article"),
    path(
        "articles/edit-article/<int:article_id>/",
        views.edit_article,
        name="edit_article",
    ),
    path(
        "articles/delete-article/<int:article_id>/",
        views.delete_article_confirm,
        name="confirm_delete_article",
    ),
    path(
        "articles/delete-article/<int:article_id>/confirmed/",
        views.delete_article,
        name="delete_article",
    ),

    # Message Management URL's
    path("messages/", views.cp_messages, name="cp_messages"),
    path(
        "messages/toggle-read/<int:message_id>/", views.toggle_read, name="toggle_read"
    ),
    path(
      "messages/view-message/<int:message_id>/",
      views.view_message,
      name="view_message"
    ),
    path(
        "messages/confirm-delete-message/<int:message_id>/",
        views.delete_message_confirm,
        name="delete_message_confirm",
    ),
    path(
        "messages/delete-message/<int:message_id>/",
        views.delete_message,
        name="delete_message",
    ),

    # Portfolio Management URL's
    path("portfolio/", views.cp_portfolio, name="cp_portfolio"),
    path(
        "portfolio/add-portfolio-image/",
        views.add_portfolio_image,
        name="add_portfolio_image",
    ),
    path(
        "portfolio/delete-portfolio-image/<int:image_id>/",
        views.delete_portfolio_image_confirm,
        name="delete_portfolio_image_confirm",
    ),
    path(
        "portfolio/delete-portfolio-image/<int:image_id>/confirmed/",
        views.delete_portfolio_image,
        name="delete_portfolio_image",
    ),

    # Review Management URL's
    path("manage-reviews/", views.manage_reviews, name="manage_reviews"),
    path("manage-reviews/add-review/", views.add_review, name="add_review"),
    path(
        "manage-reviews/delete-review/<int:review_id>/",
        views.delete_review_confirm,
        name="delete_review_confirm",
    ),
    path(
        "manage-reviews/delete-review/<int:review_id>/confirmed/",
        views.delete_review,
        name="delete_review",
    ),
    path(
        "manage-reviews/edit-review/<int:review_id>/",
        views.edit_review,
        name="edit_review",
    ),
    # Payment Management URL's
    path("manage-payments/", views.cp_payments, name="cp_payments"),
    path("manage-payments/new-payment/", views.new_payment, name="new_payment"),
    path(
        "manage-payments/view-details/<int:payment_id>/",
        views.view_payment,
        name="view_payment",
    ),

    # Analytics Paths
    path("analytics/", views.cp_analytics, name="cp_analytics"),

    # CMS Paths
    path("cms-homepage/", views.cp_cms_home, name="cp_cms_home"),

    path("cms-edit-hero/", views.cp_cms_hero, name="cp_cms_hero"),
    path("cms-edit-about-home/", views.cp_cms_about_home_edit, name="cp_cms_about_home_edit"),
    path("cms-edit-trusted-by/", views.cp_cms_trusted_by_edit, name="cp_cms_trusted_by_edit"),
    path("cms-faq-section/", views.cp_cms_faq, name="cp_cms_faq"),
    path("cms-faq-section/add-faq/", views.cms_add_faq, name="cms_add_faq"),
    path("cms-faq-section/edit-faq/<int:faq_id>/", views.cms_edit_faq, name="cms_edit_faq"),
    path("cms-faq-section/delete-faq-confirm/<int:faq_id>/", views.cms_delete_faq_confirm, name="cms_delete_faq_confirm"),
    path("cms-faq-section/delete-faq/<int:faq_id>/", views.cms_delete_faq, name="cms_delete_faq"),

    path("cms-reviews/", views.cp_cms_reviews, name="cp_cms_reviews"),
    path("cms-add-review/", views.add_cms_review, name="add_cms_review"),
    path("cms-edit-review/<int:review_id>/", views.cms_edit_review, name="cms_edit_review"),
    path("cms-delete-review-confirm/<int:review_id>/", views.cms_delete_review_confirm, name="cms_delete_review_confirm"),
    path("cms-delete-review/<int:review_id>/", views.cms_delete_review, name="cms_delete_review"),

    # Homepage Slider Image Management urls
    path("control-panel/cms/manage-slider-images/",
         views.cp_cms_manage_slider_images, name="cp_cms_manage_slider_images"),
    path("control-panel/cms/manage-slider-images/add-slider-image/",
        views.cp_cms_add_slider_image, name="cp_cms_add_slider_image"),
    path("control-panel/cms/manage-slider-images/delete-slider-image/<int:image_id>/",
        views.cp_cms_delete_slider_image_confirm, name="cp_cms_delete_slider_image_confirm",),
    path("control-panel/cms/manage-slider-images/delete-slider-image/<int:image_id>/confirmed/",
        views.cp_cms_delete_slider_image, name="cp_cms_delete_slider_image",),

 
    
    
    
    
    
    
]
