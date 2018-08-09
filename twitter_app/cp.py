from .models import PrivateMessage

def unread_msgs(request):
    unread_msgs = PrivateMessage.objects.filter(recipient=request.user,
                                                is_read=False).count()
    return {
        "unread_msgs" : unread_msgs
        }

