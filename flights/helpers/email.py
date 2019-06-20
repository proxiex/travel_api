from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import get_user_model
from django.core.mail import send_mass_mail

User = get_user_model()


def email_ticket_reminder():
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

        Regards.
    """

    reminder_message = ('Flight reminder',
                        msg_reminder,
                        'noreply@syneinc.com',
                        users_email)
    send_mass_mail((reminder_message,), fail_silently=True)
