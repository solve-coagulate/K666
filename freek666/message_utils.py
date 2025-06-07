from django_messages.models import Message
from django.utils import timezone


def send_message(sender, recipient, body, subject=""):
    """Create a new message."""
    msg = Message(
        sender=sender,
        recipient=recipient,
        subject=subject or "(no subject)",
        body=body,
        sent_at=timezone.now(),
    )
    msg.save()
    return msg


def inbox_for(user):
    return Message.objects.inbox_for(user)
