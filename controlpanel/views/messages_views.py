from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from home.models import Message


@user_passes_test(lambda u: u.is_superuser)
def cp_messages(request):
    """
    A view to return the messages page
    """
    latest_messages = Message.objects.all().order_by("-created_at")[:5]
    total_unread_messages = Message.objects.filter(read=False).count()
    unread_messages = Message.objects.filter(read=False)[:5]
    messages = Message.objects.all()

    context = {
        "form_messages": messages,
        "latest_messages": latest_messages,
        "total_unread_messages": total_unread_messages,
        "unread_messages": unread_messages,
    }
    return render(request, "messages/message-management.html", context)


@user_passes_test(lambda u: u.is_superuser)
def view_message(request, message_id):
    """
    A view to view a message
    """
    message = get_object_or_404(Message, id=message_id)
    message.read = True
    message.save()
    total_unread_messages = Message.objects.filter(read=False).count()
    unread_messages = Message.objects.filter(read=False)[:5]

    context = {
        "message": message,
        "total_unread_messages": total_unread_messages,
        "unread_messages": unread_messages,
    }
    return render(request, "messages/view-message.html", context)


@user_passes_test(lambda u: u.is_superuser)
def toggle_read(request, message_id):
    """
    A view to toggle the read status of a message
    """
    try:
        message = get_object_or_404(Message, id=message_id)
        message.read = not message.read
        message.save()
        messages.success(request, "Message status updated successfully")
    except Message.DoesNotExist:
        messages.error(request, "Message not found")
    return redirect(reverse(cp_messages))


@user_passes_test(lambda u: u.is_superuser)
def delete_message_confirm(request, message_id):
    """
    A view to confirm the deletion of a message
    """
    latest_messages = Message.objects.all().order_by("-created_at")[:5]
    total_unread_messages = Message.objects.filter(read=False).count()
    message = get_object_or_404(Message, id=message_id)
    unread_messages = Message.objects.filter(read=False)[:5]

    context = {
        "item": message,
        "latest_messages": latest_messages,
        "total_unread_messages": total_unread_messages,
        "unread_messages": unread_messages,
        "delete_path": "delete_message",
        "return_path": "cp_messages",
    }
    return render(request, "generic/delete-confirmation.html", context)


@user_passes_test(lambda u: u.is_superuser)
def delete_message(request, message_id):
    """
    A view to delete a message
    """
    try:
        get_object_or_404(Message, id=message_id).delete()
    except Exception as e:
        messages.error(request, f"There was an error deleting the message: {e}")
        return redirect(reverse(cp_messages))
    messages.success(request, "Message deleted successfully")
    return render(request, "generic/item-deleted.html")
