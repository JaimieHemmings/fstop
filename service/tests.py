from django.urls import reverse
from django.test import TestCase
import requests

BASE_URL = "http://127.0.0.1:8000"

class UrlsTest(TestCase):
    def test_event_url(self):
        path = reverse('event_services')
        print(f"Resolved Path: {path}")

    def test_lifestyle_url(self):
        path = reverse('lifestyle_services')
        print(f"Resolved Path: {path}")

    def test_property_url(self):
        path = reverse('property_services')
        print(f"Resolved Path: {path}")

    def test_aerial_url(self):
        path = reverse('aerial_services')
        print(f"Resolved Path: {path}")


class HttpResponseTest(TestCase):

    def test_event_response(self):
        path = reverse('event_services')
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_lifestyle_response(self):
        path = reverse('lifestyle_services')
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_property_response(self):
        path = reverse('property_services')
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_aerial_response(self):
        path = reverse('aerial_services')
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)