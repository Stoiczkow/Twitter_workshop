from .models import PrivateMessage

def unread_msgs(request):
    if request.user.id is not None:
        unread_msgs = PrivateMessage.objects.filter(recipient=request.user,
                                                    is_read=False).count()
        return {
            "unread_msgs" : unread_msgs
            }
    else:
        return {
            "unread_msgs": 0
        }
