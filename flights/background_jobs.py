"""Flight bkackground job module."""

from flights.helpers.decorators import start_backgroun_job
from .helpers.email import email_booking_report
import csv


@start_backgroun_job
def bg_job(start_date, end_date, user, bookings):
    """Background job."""
    file_name = f'{start_date}_{end_date}_booking_report.csv'
    with open(file_name, 'w') as booking_report:
        report = csv.writer(booking_report, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        report.writerow([
            'Username',
            'Email',
            'Flight number',
            'From',
            'To',
            'Depature Time',
            'Arrival Time',
            'Prince'])
        for booking in bookings:
            report.writerow([
                booking.user.username,
                booking.user.email,
                booking.flight.airline.flight_number,
                booking.flight.from_location,
                booking.flight.to_location,
                booking.flight.departure_time,
                booking.flight.arrival_time,
                booking.flight.price
            ])

    email_booking_report(user, start_date, end_date, file_name)
