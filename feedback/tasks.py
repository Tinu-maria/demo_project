from time import sleep
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from celery import shared_task
from django.template.loader import render_to_string
from django.utils.html import strip_tags


@shared_task()  # to transform this function into a Celery task
def send_feedback_email_task(email_address, message):
    sleep(20)  # sleep freezes Django

    html_context = render_to_string('feedback/email.html', {'message': message})
    text_content = strip_tags(html_context)
    email = EmailMultiAlternatives("Test Mail", text_content, settings.EMAIL_HOST_USER, [email_address])
    email.attach_alternative(html_context, 'text/html')
    email.send()

    # send_mail(
    #     "Test Mail",
    #     f"\t{message}\n\nThank you!",
    #     settings.EMAIL_HOST_USER,
    #     [email_address],
    #     fail_silently=False,
    # )
