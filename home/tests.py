from django.urls import reverse
from django.test import TestCase
import requests

BASE_URL = "http://127.0.0.1:8000"


class UrlsTest(TestCase):
    def test_index_url(self):
        path = reverse('home')
        print(f"Resolved Path: {path}")

    def test_about_url(self):
        path = reverse('about')
        print(f"Resolved Path: {path}")

    def test_contact_url(self):
        path = reverse('contact')
        print(f"Resolved Path: {path}")


class HttpResponseTest(TestCase):

    def test_index_response(self):
        path = reverse('home')
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_about_response(self):
        path = reverse('about')
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_contact_response(self):
        path = reverse('contact')
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)
