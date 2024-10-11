from django.test import TestCase, Client
from django.urls import reverse

class TestServicePageModel(TestCase):
    
    def setUp(self):
        self.client = Client()
    
    def test_get_service_page(self):
        response = self.client.get(
            reverse('lifestyle_services'))
        self.assertEqual(response.status_code, 200)