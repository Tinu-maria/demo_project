from time import sleep
from django.core.mail import send_mail
from django.conf import settings
from celery import shared_task

@shared_task() 
# to transform this function into a Celery task
def send_feedback_email_task(email_address, message):
        sleep(20)  # freezes Django
        send_mail(
            "Your Feedback",
            f"\t{message}\n\nThank you!",
            settings.EMAIL_HOST_USER,
            [email_address],
            fail_silently=False,
        )

