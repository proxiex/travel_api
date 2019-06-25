"""Flight bkackground job module."""

from flights.helpers.decorators import start_backgroun_job
from .models import Booking
from .helpers.email import email_booking_report
import csv


@start_backgroun_job
def bg_job(start_date, end_date, user):
    """Background job."""
    bookings = Booking.objects.filter(
        user=user,
        created_at__gte=start_date,
        created_at__lte=end_date,
        booked=True
    )
    file_name = f'{user.username}_booking_report.csv'
    with open(file_name, 'w') as booking_report:
        report = csv.writer(booking_report, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for booking in bookings:
            report.writerow([
                booking.flight.airline.flight_number,
                booking.flight.from_location,
                booking.flight.to_location,
                booking.flight.departure_time,
                booking.flight.arrival_time,
                booking.flight.price
            ])

    email_booking_report(user, start_date, end_date, file_name)
