from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from user_messages.models import Message


class UserMessagesTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.sender = User.objects.create_user(username="sender", password="pass")
        self.receiver = User.objects.create_user(username="receiver", password="pass")

    def test_compose_and_inbox_flow(self):
        self.client.login(username="sender", password="pass")
        response = self.client.post(
            reverse("messages_compose"),
            {"to": self.receiver.id, "message": "hello"},
            follow=True,
        )

        self.assertRedirects(response, reverse("messages_inbox"))
        success_messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn("Message sent", success_messages)

        self.assertEqual(Message.objects.count(), 1)
        msg = Message.objects.get()
        self.assertEqual(msg.user, self.receiver)
        self.assertEqual(msg.message, "hello")
        self.assertIsNone(msg.delivered_at)

        self.client.logout()
        self.client.login(username="receiver", password="pass")
        inbox = self.client.get(reverse("messages_inbox"))
        self.assertContains(inbox, "hello")
        msg.refresh_from_db()
        self.assertIsNotNone(msg.delivered_at)
