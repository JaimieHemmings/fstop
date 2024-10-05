from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

from blog.models import Article
from home.models import Message
from reviews.models import Review
from payments.models import Payment


@user_passes_test(lambda u: u.is_superuser)
def control_panel(request):
    """
    A view to return the control panel page
    """
    latest_messages = Message.objects.all().order_by("-created_at")[:5]
    total_unread_messages = Message.objects.filter(read=False).count()
    total_num_users = User.objects.all().count()
    total_articles = Article.objects.all().count()
    unread_messages = Message.objects.filter(read=False)[:5]

    latest_articles = Article.objects.all().order_by("-date")[:5]
    latest_users = User.objects.all().order_by("-date_joined")[:5]
    latest_reviews = Review.objects.all().order_by("-created_at")[:5]
    latest_payment_requests = Payment.objects.all().order_by("-date")[:5]
    # Build context
    context = {
        "total_num_users": total_num_users,
        "total_articles": total_articles,
        "latest_articles": latest_articles,
        "latest_users": latest_users,
        "latest_messages": latest_messages,
        "total_unread_messages": total_unread_messages,
        "unread_messages": unread_messages,
        "latest_reviews": latest_reviews,
        "latest_payment_requests": latest_payment_requests,
    }
    return render(request, "control-panel.html", context)
