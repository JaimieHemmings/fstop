# context_processors.py
from home.models import Message

def latest_unread_messages(request):
    """
    A context processor to return the latest messages
    """
    if request.user.is_superuser:
      latest_unread_messages = Message.objects.filter(read=False)[:5]
      return {
          "latest_unread_messages": latest_unread_messages,
      }
    else:
      return {
            "latest_unread_messages": "",
      }


def message_notification_num(request):
    """
    A context processor to return the number of unread messages
    """
    if request.user.is_superuser:
        total_unread_messages_num = Message.objects.filter(read=False).count()
        return {
            "total_unread_messages_num": total_unread_messages_num,
        }
    else:
        return {
            "total_unread_messages_num": "",
        }