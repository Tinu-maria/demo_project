from django.shortcuts import redirect
from django.contrib import messages
from feedback.functions import send_email
from django.contrib.auth import authenticate
from feedback.forms import LoginForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User


def signin_required(function):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "You must login to access")
            return redirect("signin")
        else:
            return function(request, *args, **kwargs)

    return wrapper


# def authentication_error(function):
#     def wrapper(request, *args, **kwargs):
#         # if not request.user.is_authenticated:
#         form = LoginForm()
#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password")
#             email = form.cleaned_data.get("email")
#             # user = authenticate(request, username=username, password=password, email=email)
#             # user = User.objects.get(username=username, password=password)
#             if not User.objects.get(username=username, password=password).exists():
#                 send_mail(
#                     "Test Mail",
#                     "We have found authentication error. Please enter correct credentials",
#                     settings.EMAIL_HOST_USER,
#                     [email],
#                     fail_silently=False,
#                 )
#                 return redirect("signin")
#         return function(request, *args, **kwargs)
#     return wrapper


