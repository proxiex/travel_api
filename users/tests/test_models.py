"""Test moduls."""

from django.test import TestCase

from users.models import CustomUser


class UserModelTestCase(TestCase):
    """This class defines the test suite for the flights model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.user = CustomUser(
            username='proxie',
            email='proxie@me.com',
            password="password")

    def test_model_can_create_a_booking(self):
        """Test the flight model can create a flight."""
        old_count = CustomUser.objects.count()
        self.user.save()
        new_count = CustomUser.objects.count()
        self.assertNotEqual(old_count, new_count)
