from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import status
from flights.helpers.decorators import start_backgroun_job
from .models import Booking
from .helpers.email import email_booking_report
import csv


@start_backgroun_job
def bg_job(start_date, end_date, user):
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


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def report(request):
    start_date = request.query_params.get('start_date')
    end_date = request.query_params.get('end_date')

    if start_date and end_date:
        bg_job(start_date, end_date, request.user)

        return Response(
            data={'message': 'Your request is processing, once your report is ready you will get an email notification!'},
            status=status.HTTP_200_OK)
    else:
        return Response(
            data={
                "error": "Start and End date are requried! e.g?end_date=2019-06-22&start_date=2018-06-22"
            },
            status=status.HTTP_400_BAD_REQUEST
        )
