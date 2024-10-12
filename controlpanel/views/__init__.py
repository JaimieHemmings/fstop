from .dashboard_views import *
from .messages_views import *
from .articles_views import *
from .payments_views import *
from .cms_homepage_views import *
from .cms_services_views import *
from .cms_portfolio_views import *
from .cms_reviews_views import *
from .cms_about_views import *
from django.contrib.auth.decorators import user_passes_test


# placeholder for analytics views until implemented
@user_passes_test(lambda u: u.is_superuser)
def cp_analytics(request):
    """
    A view to return the analytics page
    """
    return render(request, "analytics/analytics.html")
