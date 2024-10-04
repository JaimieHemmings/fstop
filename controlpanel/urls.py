from django.urls import path
from . import views

urlpatterns = [
    # Control Panel Root
    path("",
         views.control_panel,
         name="control_panel"),

    # Article Management URL's
    path("articles/",
         views.cp_articles,
         name="cp_articles"),
    path("articles/create-new/",
         views.add_article,
         name="add_article"),
    path("articles/edit-article/<int:article_id>/",
         views.edit_article,
         name="edit_article"),
    path("articles/delete-article/<int:article_id>/",
         views.delete_article_confirm,
         name="confirm_delete_article"),
    path("articles/delete-article/<int:article_id>/confirmed/",
         views.delete_article,
         name="delete_article"),

    # Message Management URL's
    path("messages/",
         views.cp_messages,
         name="cp_messages"),
    path("messages/toggle-read/<int:message_id>/",
         views.toggle_read,
         name="toggle_read"),
    path("messages/view-message/<int:message_id>/",
         views.view_message,
         name="view_message"),
    path("messages/confirm-delete-message/<int:message_id>/",
         views.delete_message_confirm,
         name="delete_message_confirm"),
    path("messages/delete-message/<int:message_id>/",
         views.delete_message,
         name="delete_message"),

    # Portfolio Management URL's
    path("portfolio/",
         views.cp_portfolio,
         name="cp_portfolio"),
    path("portfolio/add-portfolio-image/",
         views.add_portfolio_image,
         name="add_portfolio_image"),
    path("portfolio/delete-portfolio-image/<int:image_id>/",
         views.delete_portfolio_image_confirm,
         name="delete_portfolio_image_confirm"),
    path("portfolio/delete-portfolio-image/<int:image_id>/confirmed/",
         views.delete_portfolio_image,
         name="delete_portfolio_image"),

    # Payment Management URL's
    path("manage-payments/",
         views.cp_payments,
         name="cp_payments"),
    path("manage-payments/new-payment/",
         views.new_payment,
         name="new_payment"),
    path("manage-payments/view-details/<int:payment_id>/",
         views.view_payment,
         name="view_payment"),

    # Analytics Paths
    path("analytics/", views.cp_analytics, name="cp_analytics"),

    # CMS Paths
    path("cms-homepage/",
         views.cp_cms_home,
         name="cp_cms_home"),

    path("cms-edit-hero/",
         views.cp_cms_hero,
         name="cp_cms_hero"),
    path("cms-edit-about-home/",
         views.cp_cms_about_home_edit,
         name="cp_cms_about_home_edit"),
    path("cms-edit-trusted-by/",
         views.cp_cms_trusted_by_edit,
         name="cp_cms_trusted_by_edit"),
    path("cms-faq-section/",
         views.cp_cms_faq,
         name="cp_cms_faq"),
    path("cms-faq-section/add-faq/",
         views.cms_add_faq,
         name="cms_add_faq"),
    path("cms-faq-section/edit-faq/<int:faq_id>/",
         views.cms_edit_faq,
         name="cms_edit_faq"),
    path("cms-faq-section/delete-faq-confirm/<int:faq_id>/",
         views.cms_delete_faq_confirm,
         name="cms_delete_faq_confirm"),
    path("cms-faq-section/delete-faq/<int:faq_id>/",
         views.cms_delete_faq,
         name="cms_delete_faq"),

    # Reviews Management URLs
    path("cms-reviews/",
         views.cms_manage_reviews,
         name="cms_manage_reviews"),
    path("cms-add-review/",
         views.cms_add_review,
         name="add_cms_review"),
    path("cms-edit-review/<int:review_id>/",
         views.cms_edit_review,
         name="cms_edit_review"),
    path("cms-delete-review-confirm/<int:review_id>/",
         views.cms_delete_review_confirm,
         name="cms_delete_review_confirm"),
    path("cms-delete-review/<int:review_id>/",
         views.cms_delete_review,
         name="cms_delete_review"),

    # Homepage Slider Image Management URLs
    path("cms/manage-slider-images/",
         views.cp_cms_manage_slider_images,
         name="cp_cms_manage_slider_images"),
    path("cms/manage-slider-images/add-slider-image/",
         views.cp_cms_add_slider_image, name="cp_cms_add_slider_image"),
    path("cms/manage-slider-images/"
         "delete-slider-image/<int:image_id>/",
         views.cp_cms_delete_slider_image_confirm,
         name="cp_cms_delete_slider_image_confirm",),
    path("cms/manage-slider-images/"
         "delete-slider-image/<int:image_id>/confirmed/",
         views.cp_cms_delete_slider_image, name="cp_cms_delete_slider_image"),

    # Homepage About Section Management URL's
    path("cms/manage-about-section/",
         views.cp_cms_manage_about_section,
         name="cp_cms_manage_about_section"),
    path("cms/manage-about-section/add-panel/",
         views.cp_cms_add_about_section, name="cp_cms_add_about_section"),
    path("cms/manage-about-section/edit-panel/<int:panel_id>/",
         views.cp_cms_edit_about_section, name="cp_cms_edit_about_section"),
    path("cms/manage-about-section/"
         "delete-panel-confirm/<int:panel_id>/",
         views.cp_cms_delete_about_section_confirm,
         name="cp_cms_delete_about_section_confirm"),
    path("cms/manage-about-section/delete-panel/<int:panel_id>/",
         views.cp_cms_delete_about_section,
         name="cp_cms_delete_about_section"),

    # Services Management URL's
    # Path for services Overview
    path("cms/manage-services/",
         views.cp_cms_manage_services,
         name="cp_cms_manage_services"),
    # Path to edit the hero
    path("cms/manage-services/edit-hero/",
         views.cp_cms_edit_services_hero,
         name="cp_cms_edit_services_hero"),
    # Path to edit the banner
    path("cms/manage-services/edit-banner/",
         views.cp_cms_edit_services_banner,
         name="cp_cms_edit_services_banner"),
    # Path to Cards overview
    path("cms/manage-services/edit-cards/",
         views.cp_cms_edit_services_cards,
         name="cp_cms_edit_services_cards"),
    # Path to edit a single card
    path("cms/manage-services/edit-cards/edit-card/<int:card_id>/",
         views.cp_cms_edit_services_card,
         name="cp_cms_edit_services_card"),
    # Path to confirm deletion of a card
     path("cms/manage-services/edit-cards/delete-card-confirm/<int:card_id>/",
          views.cp_cms_delete_services_card_confirm,
          name="cp_cms_delete_services_card_confirm"),
     # Path to delete a card
     path("cms/manage-services/edit-cards/delete-card/<int:card_id>/",
          views.cp_cms_delete_services_card,
          name="cp_cms_delete_services_card"),
     # Path to add a new card
     path("cms/manage-services/edit-cards/add-card/",
          views.cp_cms_add_services_card,
          name="cp_cms_add_services_card"),
]
