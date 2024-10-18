from django.urls import reverse
from django.test import TestCase
import requests
from .models import Article

articles = Article.objects.all()

BASE_URL = "http://127.0.0.1:8000"


class UrlsTest(TestCase):
    def test_blog_url(self):
        path = reverse('blog')
        print(f"Resolved Path: {path}")
        response = requests.get(f"{BASE_URL}{path}")
        self.assertEqual(response.status_code, 200)

    def test_article_url(self):
        for article in articles:
            with self.subTest(article=article):
                path = reverse('article', args=[article.slug])
                response = requests.get(f"{BASE_URL}{path}")
                self.assertEqual(response.status_code, 200)
