from django.test import TestCase
from flights.models import Airline, Flight, Booking
from users.models import CustomUser


class BookingtModelTestCase(TestCase):
    """This class defines the test suite for the flights model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.user = CustomUser(
            username='proxie',
            email='proxie@me.com',
            password="password")

        self.user.save()

        self.airline = Airline(
            name="KLM",
            flight_number="A360"
        )

        self.airline.save()

        self.flight = Flight(
            airline=self.airline,
            from_location='Jos',
            to_location='Lagos',
            departure_time='2019-06-14 02:33:00+01',
            arrival_time='2019-06-14 02:33:00+01',
            price=21000,
            no_of_seats=100
        )
        self.flight.save()

    def test_model_can_create_a_booking(self):
        """Test the flight model can create a flight."""
        old_count = Booking.objects.count()

        Booking.objects.create(
            flight=self.flight,
            user=self.user
        )
        self.flight.save()
        new_count = Booking.objects.count()
        self.assertNotEqual(old_count, new_count)


class FlightModelTestCase(TestCase):
    """This class defines the test suite for the flights model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.airline = Airline(
            name="KLM",
            flight_number="A360"
        )

        self.airline.save()

        self.flight = Flight(
            airline=self.airline,
            from_location='Jos',
            to_location='Lagos',
            departure_time='2019-06-14 02:33:00+01',
            arrival_time='2019-06-14 02:33:00+01',
            price=21000,
            no_of_seats=100
        )

    def test_model_can_create_a_booking(self):
        """Test the flight model can create a flight."""
        old_count = Flight.objects.count()
        self.flight.save()
        new_count = Flight.objects.count()
        self.assertNotEqual(old_count, new_count)
