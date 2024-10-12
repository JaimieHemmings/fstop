from django.urls import path
from . import views

urlpatterns = [
    # Control Panel Root
    path("", views.control_panel, name="control_panel"),
    # Admin URLs
    # Message Management URL's
    path("messages/", views.cp_messages, name="cp_messages"),
    path(
        "messages/<int:message_id>/toggle-read/",
        views.toggle_read, name="toggle_read"
    ),
    path("messages/<int:message_id>/",
         views.view_message, name="view_message"),
    path(
        "messages/<int:message_id>/delete/",
        views.delete_message_confirm,
        name="delete_message_confirm",
    ),
    path(
        "messages/<int:message_id>/delete/confirmed/",
        views.delete_message,
        name="delete_message",
    ),
    # Article Management URL's
    path("articles/", views.cp_articles, name="cp_articles"),
    path("articles/new/", views.add_article, name="add_article"),
    path(
        "articles/<int:article_id>/edit/",
        views.edit_article, name="edit_article"),
    path(
        "articles/<int:article_id>/delete/",
        views.delete_article_confirm,
        name="confirm_delete_article",
    ),
    path(
        "articles/<int:article_id>/delete/confirmed/",
        views.delete_article,
        name="delete_article",
    ),
    # Payment Management URL's
    path("payments/", views.cp_payments, name="cp_payments"),
    path("payments/new/", views.new_payment, name="new_payment"),
    path(
         "payments/<int:payment_id>/",
         views.view_payment, name="view_payment"),
    # Analytics Paths
    path("analytics/", views.cp_analytics, name="cp_analytics"),
    # CMS Paths for homepage
    path("homepage/", views.cp_cms_home, name="cp_cms_home"),
    path("homepage/hero/", views.cp_cms_hero, name="cp_cms_hero"),
    path(
        "homepage/hero/edit/",
        views.cp_cms_about_home_edit,
        name="cp_cms_about_home_edit",
    ),
    path(
        "trusted-by/edit/", views.cp_cms_trusted_by_edit,
        name="cp_cms_trusted_by_edit"
    ),
    path("homepage/faq/", views.cp_cms_faq, name="cp_cms_faq"),
    path("homepage/faq/new/", views.cms_add_faq, name="cms_add_faq"),
    path(
        "homepage/faq/<int:faq_id>/edit/",
        views.cms_edit_faq, name="cms_edit_faq"),
    path(
        "homepage/faq/<int:faq_id>/delete/",
        views.cms_delete_faq_confirm,
        name="cms_delete_faq_confirm",
    ),
    path(
        "homepage/faq/<int:faq_id>/delete/confirmed/",
        views.cms_delete_faq,
        name="cms_delete_faq",
    ),
    path(
        "homepage/services/",
        views.cp_cms_manage_about_section,
        name="cp_cms_manage_about_section",
    ),
    path(
        "homepage/services/new/",
        views.cp_cms_add_about_section,
        name="cp_cms_add_about_section",
    ),
    path(
        "homepage/services/<int:panel_id>/edit/",
        views.cp_cms_edit_about_section,
        name="cp_cms_edit_about_section",
    ),
    path(
        "homepage/services/<int:panel_id>/delete/",
        views.cp_cms_delete_about_section_confirm,
        name="cp_cms_delete_about_section_confirm",
    ),
    path(
        "homepage/services/<int:panel_id>/delete/confirmed/",
        views.cp_cms_delete_about_section,
        name="cp_cms_delete_about_section",
    ),
    # Homepage Carousel Image Management URLs
    path(
        "homepage/carousel-images/",
        views.cp_cms_manage_slider_images,
        name="cp_cms_manage_slider_images",
    ),
    path(
        "homepage/carousel-images/new/",
        views.cp_cms_add_slider_image,
        name="cp_cms_add_slider_image",
    ),
    path(
        "homepage/carousel-images/<int:image_id>/delete/",
        views.cp_cms_delete_slider_image_confirm,
        name="cp_cms_delete_slider_image_confirm",
    ),
    path(
        "homepage/carousel-images/<int:image_id>/delete/confirmed/",
        views.cp_cms_delete_slider_image,
        name="cp_cms_delete_slider_image",
    ),

    # CMS paths for the about page
    path("about/edit",
         views.cp_cms_about_edit,
         name="cp_cms_about_edit"),   

    # CMS Paths for services page
    path("services-pages/",
        views.cp_cms_manage_services,
        name="cp_cms_manage_services"),

    path("services-pages/edit/lifestyle/",
        views.cp_cms_edit_lifestyle,
        name="cp_cms_edit_lifestyle"),

    path("services-pages/edit/event-product/",
        views.cp_cms_edit_event,
        name="cp_cms_edit_event"),

    path("services-pages/edit/property-product/",
        views.cp_cms_edit_property,
        name="cp_cms_edit_property"),

    path("services-pages/edit/aerial-product/",
        views.cp_cms_edit_aerial,
        name="cp_cms_edit_aerial"),

    # Portfolio page URL's
    path("portfolio/", views.cp_portfolio, name="cp_portfolio"),
    path(
        "portfolio/new/",
        views.add_portfolio_image,
        name="add_portfolio_image"),
    path(
        "portfolio/<int:image_id>/delete/",
        views.delete_portfolio_image_confirm,
        name="delete_portfolio_image_confirm",
    ),
    path(
        "portfolio/<int:image_id>/delete/confirmed/",
        views.delete_portfolio_image,
        name="delete_portfolio_image",
    ),
    # Reviews Management URLs
    path("reviews/", views.cms_manage_reviews, name="cms_manage_reviews"),
    path("reviews/add", views.cms_add_review, name="add_cms_review"),
    path(
        "reviews/<int:review_id>/edit/",
        views.cms_edit_review, name="cms_edit_review"
    ),
    path(
        "reviews/<int:review_id>/delete/",
        views.cms_delete_review_confirm,
        name="cms_delete_review_confirm",
    ),
    path(
        "reviews/<int:review_id>/delete/confirmed/",
        views.cms_delete_review,
        name="cms_delete_review",
    ),
]
