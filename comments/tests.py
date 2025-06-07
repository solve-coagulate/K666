import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "comments.test_settings")
import django
django.setup()

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client

from .models import Comment, SUBJECT_LENGTH


class TestCommentModel(TestCase):
    """Tests for the :class:`Comment` model helper methods."""

    def setUp(self):
        self.user = get_user_model().objects.create_user(username="tester")

    def make_comment(self, text):
        return Comment(text=text, created_by=self.user)

    def test_subject_and_body_short_single_line(self):
        """A short single line should be the subject and leave an empty body."""
        comment = self.make_comment("Hello World")

        self.assertEqual(comment.subject(), "Hello World")
        self.assertEqual(comment.body(), "")

    def test_subject_truncates_long_first_line(self):
        """First line longer than SUBJECT_LENGTH is truncated with ellipsis."""
        long_text = "A" * (SUBJECT_LENGTH + 10)
        comment = self.make_comment(long_text)

        self.assertEqual(
            comment.subject(),
            "A" * SUBJECT_LENGTH + "...",
        )
        self.assertEqual(comment.body(), "A" * 10)

    def test_body_multiline(self):
        """Body should contain text after a blank line separation."""
        text = "Subject line\n\nBody line 1\nBody line 2"
        comment = self.make_comment(text)

        self.assertEqual(comment.subject(), "Subject line")
        self.assertEqual(comment.body(), "Body line 1\nBody line 2")

    def test_windows_line_endings(self):
        """Windows newlines should be normalised when splitting."""
        text = "Subject\r\n\r\nBody"
        comment = self.make_comment(text)

        self.assertEqual(comment.subject(), "Subject")
        self.assertEqual(comment.body(), "Body")

    def test_replies_counts_descendants(self):
        """`replies` should count all descendant comments."""
        root = Comment.objects.create(text="root", created_by=self.user)
        child1 = Comment.objects.create(text="c1", created_by=self.user, parent=root)
        child2 = Comment.objects.create(text="c2", created_by=self.user, parent=root)
        Comment.objects.create(text="gc", created_by=self.user, parent=child1)

        self.assertEqual(root.replies(), 3)
        self.assertEqual(child1.replies(), 1)
        self.assertEqual(child2.replies(), 0)

    def test_replies_unsaved_comment(self):
        """Unsaved comments have no replies."""
        comment = self.make_comment("temp")
        self.assertEqual(comment.replies(), 0)


class TestAjaxEndpoints(TestCase):
    def setUp(self):
        self.client = Client(enforce_csrf_checks=True)
        User = get_user_model()
        self.user = User.objects.create_user(username="ajaxer", password="pass")
        self.client.force_login(self.user)
        from django.middleware.csrf import _get_new_csrf_string
        self.csrf = _get_new_csrf_string()
        self.client.cookies['csrftoken'] = self.csrf

    def post(self, urlname, data):
        return self.client.post(
            reverse(urlname),
            data,
            HTTP_X_CSRFTOKEN=self.csrf,
        )

    def test_ajax_preview(self):
        response = self.post("ajax-preview-comment", {"comment_text": "preview"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Comment.objects.count(), 0)
        self.assertIn("html", response.json())

    def test_ajax_add_creates_comment(self):
        response = self.post("ajax-add-comment", {"comment_text": "new comment"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Comment.objects.count(), 1)

    def test_ajax_comment_form(self):
        response = self.post("ajax-comment-form", {"comment_text": "text"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("textarea", response.json()["html"])

    def test_ajax_comment_form_allows_empty_text(self):
        """The comment form endpoint should accept empty text."""
        response = self.post("ajax-comment-form", {"comment_text": ""})
        self.assertEqual(response.status_code, 200)
        self.assertIn("textarea", response.json()["html"])

    def test_ajax_add_validation(self):
        response = self.post("ajax-add-comment", {})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Comment.objects.count(), 0)


class StoryViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="viewer", password="pass")

    def test_story_list_and_detail(self):
        story = Comment.objects.create(text="Test story\n\nBody", created_by=self.user)
        resp = self.client.get(reverse('story-list'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, story.subject())
        detail = self.client.get(reverse('story-detail', args=[story.id]))
        self.assertEqual(detail.status_code, 200)
        self.assertContains(detail, story.subject())

    def test_user_signup_flow(self):
        resp = self.client.post(reverse('account_signup'), {
            'username': 'newuser',
            'email': 'new@example.com',
            'password1': 'pass12345',
            'password2': 'pass12345',
        })
        self.assertEqual(resp.status_code, 302)
        self.assertTrue(get_user_model().objects.filter(username='newuser').exists())


class AddCommentViewTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username="poster", password="pass")
        self.client.login(username="poster", password="pass")

    def test_add_comment_redirects_and_saves(self):
        resp = self.client.post(
            reverse("add-comment"),
            {"comment_text": "My first post", "post": "1"},
        )
        self.assertEqual(Comment.objects.count(), 1)
        comment = Comment.objects.get()
        self.assertRedirects(
            resp,
            reverse("story-detail", kwargs={"id": comment.id}),
        )

    def test_authenticated_post_creates_comment_and_redirects(self):
        resp = self.client.post(
            reverse("add-comment"),
            {"comment_text": "Another post", "post": "1"},
        )
        self.assertEqual(Comment.objects.count(), 1)
        comment = Comment.objects.get()
        self.assertRedirects(
            resp,
            reverse("story-detail", kwargs={"id": comment.id}),
        )
