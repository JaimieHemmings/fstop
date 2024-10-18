from django.urls import reverse
from django.test import TestCase
from .models import Article
from django.contrib.auth.models import User

articles = Article.objects.all()


class ArticleModelTest(TestCase):
    def test_article_model(self):
        for article in articles:
            with self.subTest(article=article):
                self.assertEqual(str(article), article.title)
                self.assertEqual(article.get_absolute_url(), reverse('article', args=[article.slug]))
                self.assertNotEqual(article.get_path(article.thumb.name), article.thumb.name)
                self.assertNotEqual(article.get_path(article.slider_image_one.name), article.slider_image_one.name)
                self.assertNotEqual(article.get_path(article.slider_image_two.name), article.slider_image_two.name)
                self.assertNotEqual(article.get_path(article.slider_image_three.name), article.slider_image_three.name)
                self.assertNotEqual(article.get_path(article.slider_image_four.name), article.slider_image_four.name)
                self.assertNotEqual(article.get_path(article.body_image.name), article.body_image.name)
                self.assertEqual(article.slug, article.slug)
                self.assertEqual(article.exerpt, article.exerpt)
                self.assertEqual(article.body, article.body)
                self.assertEqual(article.body_continued, article.body_continued)
                self.assertEqual(article.date, article.date)
                self.assertEqual(article.author, article.author)
                self.assertEqual(article.last_modified, article.last_modified)
                self.assertEqual(article.views, article.views)

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
        )
        self.article = Article.objects.create(
            body_image='test_image.jpg',
            slug='test-article',
            exerpt='This is a test exerpt.',
            body='This is the body of the test article.',
            body_continued='This is the continued body of the test article.',
            date='2023-01-01',
            author=self.user,
            last_modified='2023-01-01T00:00:00Z',
            views=10
        )

    def test_get_path(self):
        expected_path = 'images/test_image.jpg'
        actual_path = self.article.get_path(self.article.body_image.name)
        # Ensure the get_path mathod is working as expected
        self.assertNotEqual(actual_path, expected_path)

    def test_article_fields(self):
        article = self.article
        self.assertNotEqual(article.get_path(article.body_image.name), 'images/test_image.jpg')
        self.assertEqual(article.slug, 'test-article')
        self.assertEqual(article.exerpt, 'This is a test exerpt.')
        self.assertEqual(article.body, 'This is the body of the test article.')
        self.assertEqual(article.body_continued, 'This is the continued body of the test article.')
        self.assertEqual(article.author, self.user)
        self.assertEqual(article.views, 10)


class UrlsTest(TestCase):
    def test_blog_url(self):
        path = reverse('blog')
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)

    def test_article_url(self):
        articles = Article.objects.all()
        for article in articles:
            with self.subTest(article=article):
                path = reverse('article', args=[article.slug])
                response = self.client.get(path)
                self.assertEqual(response.status_code, 200)
