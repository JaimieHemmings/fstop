from django.contrib import admin
from django.urls import path, include, reverse
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import sitemaps
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from blog.models import Article

info_dict = {
    "queryset": Article.objects.all(),
    "date_field": "date",
}

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "weekly"

    def items(self):
        return ["home", "about", "services", "contact"]

    def location(self, item):
        return reverse(item)

sitemaps = {
    "static": StaticViewSitemap,
    "blog": GenericSitemap(info_dict, priority=0.6),
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("home.urls")),
    path("portfolio/", include("portfolio.urls")),
    path("blog/", include("blog.urls")),
    path("control-panel/", include("controlpanel.urls")),
    path("payments/", include("payments.urls")),
    path("profile/", include("profiles.urls")),
    path("services/", include("services.urls")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps },
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("cypress/", include("django_cypress.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
