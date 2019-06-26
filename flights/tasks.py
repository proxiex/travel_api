"""Clery task."""

from django.contrib.auth import get_user_model
from celery import shared_task

from .helpers.email import email_ticket_reminder

User = get_user_model()


@shared_task
def email_flight_remainder_task():
    """Task to send flight reminder to passengers flying in 24 hours.

    :return:
    """
    return email_ticket_reminder()
