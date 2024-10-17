from django.test import TestCase


class TestViews(TestCase):
    def test_get_portfolio_page(self):
        page = self.client.get("/portfolio/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "portfolio.html")
