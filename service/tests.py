from django.test import TestCase, Client
from django.urls import reverse

class TestServicePageModel(TestCase):
    
    def setUp(self):
        self.client = Client()
    
    def test_get_service_page(self):
        # List of named URLs
        urls = [
            'lifestyle_services',
            'aerial_services',
            'property_services',
            'event_services'
        ]

        for url in urls:
            with self.subTest(url=url):
                response = self.client.get(reverse(url))
                self.assertEqual(response.status_code, 200)