import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "comments.test_settings")
import django
django.setup()

from django.test import TestCase
from django.contrib.auth import get_user_model

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

    def test_reply_counts(self):
        """``replies`` should count all descendant comments."""

        root = Comment.objects.create(text="root", created_by=self.user)
        child1 = Comment.objects.create(text="c1", created_by=self.user, parent=root)
        Comment.objects.create(text="c2", created_by=self.user, parent=root)
        Comment.objects.create(text="c3", created_by=self.user, parent=child1)

        self.assertEqual(root.replies(), 3)
        self.assertEqual(child1.replies(), 1)

