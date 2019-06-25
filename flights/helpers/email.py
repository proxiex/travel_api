"""Email module."""

from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mass_mail

User = get_user_model()


def email_ticket_reminder():
    """Email Flight ticket."""
    date_time = timezone.now() + timedelta(days=1)
    users = User.objects.filter(
        booking__flight__departure_time__lte=date_time,
        booking__flight__departure_time__gte=timezone.now(),
        booking__booked=True
    )

    users_email = [user.email for user in users]

    msg_reminder = """
        Dear Customer,

        This is to remind you of your Syne Inc flight in the next 24 hours.
        Please check your booking confirmation email for flight details.

        Regards.
    """

    reminder_message = ('Flight reminder',
                        msg_reminder,
                        'noreply@syneinc.com',
                        users_email)
    send_mass_mail((reminder_message,), fail_silently=True)


def email_flight_details(booking):
    """Email Fight details."""
    html_content = render_to_string('emails/bookkng_email.html', {'booking': booking})
    text_content = strip_tags(html_content)

    msg = EmailMultiAlternatives('Flight details', text_content, 'noreply@syneinc.com', [booking.user.email])

    msg.attach_alternative(html_content, "text/html")
    msg.send()


def email_booking_report(user, end_date, start_date, file):
    """Email booking report to user."""
    subject, from_email, to = 'Booking Report', 'noreply@syneinc.com', user.email
    text_content = f'Pls find attached your booking report from {start_date} to {end_date}'
    html_content = f'<p>Pls find attached your booking report from {start_date} to {end_date}.</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_file(file)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
