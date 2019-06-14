from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Airline(models.Model):
    """
    Airline model deffinatioon.
    """
    name = models.CharField(
        max_length=100,
        verbose_name='Airline Name'
    )
    flight_number = models.CharField(
        max_length=100,
        verbose_name='Flight Numbrer'
    )

    def __str__(self):
        return '{} - {}'.format(self.name, self.flight_number)


class Flight(models.Model):
    """
     Flight model definition.
    """
    from_location = models.CharField(
        max_length=100,
        verbose_name='From Location'
    )
    to_location = models.CharField(
        max_length=100,
        verbose_name='To Location'
    )
    departure_time = models.DateTimeField(
        verbose_name='Departure time'
    )
    arrival_time = models.DateTimeField(
        verbose_name='Arrival Time'
    )
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    no_of_seats = models.IntegerField()

    price = models.IntegerField(default=0)

    passengers = models.ManyToManyField(
        User,
        through='Booking',
        through_fields=('flight', 'user')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created At'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated At'
    )

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return 'From {} to {} - {}'.format(self.from_location, self.to_location, self.airline)


class Booking(models.Model):
    """
    Booking model defination.
    """
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booked = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created At'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated At'
    )

    def __str__(self):
        return '{}'.format(self.flight)
