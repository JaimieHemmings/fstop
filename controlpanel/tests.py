from django.urls import reverse
from django.test import TestCase
import requests

BASE_URL = "http://127.0.0.1:8000"


class UrlsTest(TestCase):
    # Test URL's that do not require parameters

    def test_controlpanel_url(self):
        path = reverse('control_panel')
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_message_management_url(self):
        path = reverse('cp_messages')
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_article_management_url(self):
        path = reverse('cp_articles')
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_article_add_url(self):
        path = reverse('add_article')
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_payment_management_url(self):
        path = reverse('cp_payments')
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_payment_add_url(self):
        path = reverse('new_payment')
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_analytics_url(self):
        path = reverse('cp_analytics')
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_cms_home_url(self):
        path = reverse('cp_cms_home')
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_cms_hero_url(self):
        path = reverse('cp_cms_hero')
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_cms_add_faq_url(self):
        path = reverse('cms_add_faq')
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_cp_cms_faq_url(self):
        path = reverse('cp_cms_faq')
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_cp_cms_manage_about_section_url(self):
        path = reverse('cp_cms_manage_about_section')
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_cp_cms_add_about_section_url(self):
        path = reverse('cp_cms_add_about_section')
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_cp_cms_manage_slider_images_url(self):
        path = reverse('cp_cms_manage_slider_images')
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_cp_cms_add_slider_image_url(self):
        path = reverse('cp_cms_add_slider_image')
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_cp_cms_about_edit_url(self):
        path = reverse('cp_cms_about_edit')
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_cp_cms_manage_services_url(self):
        path = reverse('cp_cms_manage_services')
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_cp_cms_edit_lifestyle_url(self):
        path = reverse('cp_cms_edit_lifestyle')
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_cp_cms_edit_event_url(self):
        path = reverse('cp_cms_edit_event')
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_cp_cms_edit_property_url(self):
        path = reverse('cp_cms_edit_property')
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_cp_cms_edit_aerial_url(self):
        path = reverse('cp_cms_edit_aerial')
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_add_portfolio_image_url(self):
        path = reverse('add_portfolio_image')
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_cms_manage_reviews_url(self):
        path = reverse('cms_manage_reviews')
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_add_cms_review_url(self):
        path = reverse('add_cms_review')
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    # Test URL's that require parameters
    def test_toggle_read_url(self):
        path = reverse('toggle_read', kwargs={'message_id': 1})
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_view_message_url(self):
        path = reverse('view_message', kwargs={'message_id': 1})
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_delete_message_confirm_url(self):
        path = reverse('delete_message_confirm', kwargs={'message_id': 1})
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_delete_message_url(self):
        path = reverse('delete_message', kwargs={'message_id': 1})
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_edit_article_url(self):
        path = reverse('edit_article', kwargs={'article_id': 1})
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_confirm_delete_article_url(self):
        path = reverse('confirm_delete_article', kwargs={'article_id': 1})
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_view_payment_url(self):
        path = reverse('view_payment', kwargs={'payment_id': 1})
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_cp_cms_about_home_edit_url(self):
        path = reverse('cp_cms_about_home_edit')
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_cp_cms_trusted_by_edit_url(self):
        path = reverse('cp_cms_trusted_by_edit')
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_cms_edit_faq_url(self):
        path = reverse('cms_edit_faq', kwargs={'faq_id': 1})
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_cms_delete_faq_confirm_url(self):
        path = reverse('cms_delete_faq_confirm', kwargs={'faq_id': 1})
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_cms_delete_faq_url(self):
        path = reverse('cms_delete_faq', kwargs={'faq_id': 1})
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_cp_cms_edit_about_section_url(self):
        path = reverse('cp_cms_edit_about_section', kwargs={'panel_id': 1})
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_cp_cms_delete_about_section_confirm_url(self):
        path = reverse(
            'cp_cms_delete_about_section_confirm', kwargs={'panel_id': 1})
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_cp_cms_delete_about_section_url(self):
        path = reverse('cp_cms_delete_about_section', kwargs={'panel_id': 1})
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_cp_cms_delete_slider_image_confirm_url(self):
        path = reverse(
            'cp_cms_delete_slider_image_confirm', kwargs={'image_id': 1})
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_cp_cms_delete_slider_image_url(self):
        path = reverse('cp_cms_delete_slider_image', kwargs={'image_id': 1})
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_delete_portfolio_image_confirm_url(self):
        path = reverse(
            'delete_portfolio_image_confirm', kwargs={'image_id': 1})
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_delete_portfolio_image_url(self):
        path = reverse('delete_portfolio_image', kwargs={'image_id': 1})
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_cms_edit_review_url(self):
        path = reverse('cms_edit_review', kwargs={'review_id': 1})
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_cms_delete_review_confirm_url(self):
        path = reverse('cms_delete_review_confirm', kwargs={'review_id': 1})
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_cms_delete_review_url(self):
        path = reverse('cms_delete_review', kwargs={'review_id': 1})
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)
