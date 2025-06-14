from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from django_messages.models import Message


class UserMessagesTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.sender = User.objects.create_user(username="sender", password="pass")
        self.receiver = User.objects.create_user(username="receiver", password="pass")

    def test_compose_and_inbox_flow(self):
        self.client.login(username="sender", password="pass")
        response = self.client.post(
            reverse("messages_compose"),
            {
                "recipient": self.receiver.username,
                "subject": "Hello",
                "body": "hello",
            },
            follow=True,
        )

        self.assertRedirects(response, reverse("messages_inbox"))
        success_messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn("Message successfully sent.", success_messages)

        self.assertEqual(Message.objects.count(), 1)
        msg = Message.objects.get()
        self.assertEqual(msg.recipient, self.receiver)
        self.assertEqual(msg.body, "hello")
        self.assertIsNone(msg.read_at)

        self.client.logout()
        self.client.login(username="receiver", password="pass")
        inbox = self.client.get(reverse("messages_inbox"))
        self.assertContains(inbox, "Hello")
        msg.refresh_from_db()
        self.assertIsNone(msg.read_at)


class AuthFlowTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username="authuser", password="pass")

    def test_login_authenticates_user(self):
        response = self.client.post(
            reverse('account_login'),
            {'login': self.user.username, 'password': 'pass'},
            follow=True,
        )
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_logout_clears_session(self):
        self.client.login(username=self.user.username, password='pass')
        self.client.post(reverse('account_logout'), follow=True)
        resp = self.client.get(reverse('story-list'))
        self.assertFalse(resp.wsgi_request.user.is_authenticated)

    def test_update_email(self):
        self.client.login(username=self.user.username, password='pass')
        resp = self.client.post(
            reverse('account_email'),
            {'action_add': '', 'email': 'new@example.com'},
        )
        self.assertEqual(resp.status_code, 302)

        self.client.post(
            reverse('account_email'),
            {'action_primary': '', 'email': 'new@example.com'},
        )
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, 'new@example.com')


class AdminAccessTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.admin = User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="pass",
        )

    def test_admin_index_accessible(self):
        self.assertTrue(
            self.client.login(username="admin", password="pass")
        )
        response = self.client.get(reverse("admin:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Django administration")


class MessageUtilsTests(TestCase):
    """Tests for helper functions in :mod:`freek666.message_utils`."""

    def setUp(self):
        User = get_user_model()
        self.sender = User.objects.create_user(username="from", password="pass")
        self.recipient = User.objects.create_user(username="to", password="pass")

    def test_send_message_and_inbox(self):
        from . import message_utils

        msg = message_utils.send_message(
            sender=self.sender,
            recipient=self.recipient,
            body="hi there",
            subject="greeting",
        )

        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(msg.subject, "greeting")
        self.assertEqual(msg.recipient, self.recipient)

        inbox = list(message_utils.inbox_for(self.recipient))
        self.assertEqual(inbox, [msg])


class ProfileViewTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username="viewer", password="pass")

    def test_profile_requires_login(self):
        resp = self.client.get(reverse("account_profile"))
        self.assertEqual(resp.status_code, 302)
        self.assertIn("/accounts/login", resp.url)

    def test_profile_displays_username(self):
        self.client.login(username="viewer", password="pass")
        resp = self.client.get(reverse("account_profile"))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Hello viewer")
