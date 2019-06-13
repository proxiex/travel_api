from django.test import TestCase

from users.models import CustomUser


class FlightModelTestCase(TestCase):
    """This class defines the test suite for the flights model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.destination = 'dest'
        self.booked_flight = CustomUser(
            username='proxie',
            email='proxie@me.com',
            password="password")

    def test_model_can_create_a_booking(self):
        """Test the flight model can create a flight."""
        old_count = CustomUser.objects.count()
        self.booked_flight.save()
        new_count = CustomUser.objects.count()
        self.assertNotEqual(old_count, new_count)
