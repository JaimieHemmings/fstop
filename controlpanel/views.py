from django.shortcuts import render
from django.contrib.auth.models import User
from blog.models import Article
from home.models import Message
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.contrib import messages

"""
This file contains the views for the control panel
All views require the user to be logged in and a superuser
"""

@login_required
@user_passes_test(lambda u: u.is_superuser)
def control_panel(request):
    """
    A view to return the control panel page
    """
    context = {}

    # Get the number of registered users
    number_of_users = User.objects.all().count()
    context["number_of_users"] = number_of_users

    number_of_articles = Article.objects.all().count()
    context["number_of_articles"] = number_of_articles

    latest_articles = Article.objects.all().order_by('-date')[:5]
    context["latest_articles"] = latest_articles

    latest_users = User.objects.all().order_by('-date_joined')[:5]
    context["latest_users"] = latest_users

    # Get the lastest messages
    latest_messages = Message.objects.all().order_by('-created_at')[:5]
    context["latest_messages"] = latest_messages

    # Get the number of unread messages
    unread_messages = Message.objects.filter(read=False).count()
    context["unread_messages"] = unread_messages

    return render(request, 'control-panel.html', context)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def cp_articles(request):
    """
    A view to return the articles page
    """
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'article-management.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def cp_messages(request):
    """
    A view to return the messages page
    """
    messages = Message.objects.all()

    context = {
        'formMessages': messages,
    }

    return render(request, 'message-management.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def toggle_read(request, message_id):
    """
    A view to toggle the read status of a message
    """
    message = Message.objects.get(id=message_id)
    message.read = not message.read
    message.save()
    messages.success(request, 'Message status updated successfully')

    return cp_messages(request)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_message_confirm(request, message_id):
    """
    A view to confirm the deletion of a message
    """
    context = {}
    message = Message.objects.get(id=message_id)
    context['message'] = message


    return render(request, 'delete-message-confirm.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_message(request, message_id):
    """
    A view to delete a message
    """
    message = Message.objects.get(id=message_id)
    message.delete()
    messages.success(request, 'Message deleted successfully')

    return cp_messages(request)