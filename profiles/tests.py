from django.test import TestCase
from django.urls import reverse
import requests

BASE_URL = "http://127.0.0.1:8000"

# Create your tests here.
class UrlsTest(TestCase):
    def test_profile_url(self):
        path = reverse('profile_page')
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_make_payment_url(self):
        path = reverse('make_payment', args=[1])
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_payment_success_url(self):
        path = reverse('payment_success', args=[1])
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)
