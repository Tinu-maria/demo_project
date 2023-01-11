from datetime import date


def get_today():
    return date.today()


def mock_date():
    day = get_today()
    return day


# from django.core.mail import send_mail
# from django.conf import settings

# def send_email(email):
#     send_mail(
#         "Test Mail",
#         "We have found authentication error",
#         settings.EMAIL_HOST_USER,
#         [email],
#         fail_silently=False,
#     )
