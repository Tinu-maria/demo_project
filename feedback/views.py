from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View, ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from feedback.models import Profile
from feedback.forms import FeedbackForm, RegistrationForm, LoginForm, ProfileForm
from django.contrib.auth.models import User
import logging
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.decorators import method_decorator
from feedback.decorators import signin_required
from django.core.paginator import Paginator
from django.db.models import F, Value, CharField
from django.db.models.functions import Concat
from django.views.decorators.cache import cache_page
from django.core.cache import cache


class RegisterView(View):
    """
    Registration view
    In GET: Returns a registration page
    In POST: Creates a new user and redirect to login page
    """
    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        return render(request, "feedback/registration.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            messages.success(request, "New user created")
            return redirect("signin")
        else:
            messages.error(request, "Invalid credentials")
            return redirect('signin')


class LoginView(View):
    """
    Login view
    In GET: Returns a login page
    In POST: Authenticate the user, sets cookies and then redirect to home page
    """
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, "feedback/login.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            email = form.cleaned_data.get("email")
            user = authenticate(request, username=username, password=password, email=email)
            if user:
                # request.session['username'] = username
                # print(request.session['username'])
                login(request, user)
                context = {
                    'username': username
                }
                messages.success(request, "Successfully logged in")
                response = render(request, "feedback/index.html", context)
                response.set_cookie('username', username)
                return response
            else:
                messages.error(request, "Invalid credentials")
                return redirect('signin')


@method_decorator(signin_required, name="dispatch")
class LogoutView(View):
    """
    Logout view
    User gets logged out and delete cookies
    """
    def get(self, request, *args, **kwargs):
        # if 'username' in request.session:
        #     request.session.flush()
        logout(request)
        response = redirect("signin")
        response.delete_cookie('username')
        return response


@method_decorator(signin_required, name="dispatch")
class FeedbackFormView(FormView):
    """
    Feedback view
    Sends a feedback message using html email
    Celery is added to schedule time
    """
    template_name = "feedback/feedback.html"
    form_class = FeedbackForm
    success_url = "/success/"

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class SuccessView(TemplateView):
    """
    Success View returns a thankyou message after feedback sending
    """
    template_name = "feedback/success.html"


log = logging.getLogger('log')


def index(request):
    """
    Index view
    Returns a home page
    Also added loggers and complex queries
    """
    log.info("Message for information")
    log.warning("Message for warning")
    log.error("Message for error")
    log.critical("Message for critical error")

    name = User.objects.annotate(
        full_name=Concat(F('first_name'), Value(' '), F('last_name'), output_field=CharField())
    )
    for n in name:
        print(n.full_name)
    # name = User.objects.aggregate(full_name = Sum(F('first_name') + F('last_name'), output_field=CharField()))
    # print(name['full_name'])

    if 'username' in request.COOKIES:
        context = {
            'username': request.COOKIES['username']
        }
        return render(request, 'feedback/index.html', context)
    else:
        return render(request, 'feedback/index.html')


@method_decorator(signin_required, name="dispatch")
class UserProfileAdd(View):
    """
    User Profile add view
    In GET: Returns a file upload page
    In POST: Creates a profile with single/multiple images and returns success page
    """

    def get(self, request, *args, **kwargs):
        form = ProfileForm()
        return render(request, 'feedback/adduserprofile.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            files = request.FILES.getlist('files')
            for file in files:
                new_file = Profile.objects.create(image=file, title=title)
                new_file.save()
            return redirect('success')


class UserProfileView(ListView):
    """
    User Profile list view
    Returns all the uploaded images
    """
    model = Profile
    template_name = 'feedback/viewuserprofile.html'
    context_object_name = 'profiles'


def pagination(request):
    """
    Pagination view
    User details are separated to different pages
    to display one page of results at a time.
    """
    # if 'username' in request.session:
    user = User.objects.get_queryset().order_by('id')
    p = Paginator(user, 1)  # p = Paginator(list_of_objects, no_of_objects_per_page)
    page_num = request.GET.get('page', 1)
    page = p.page(page_num)
    context = {'user': page}
    return render(request, 'feedback/page.html', context)
    # return redirect("signin")


@cache_page(60 * 10)
def cache_view(request):
    cache_key = "abcdefg"
    cache_time = 600  # time in seconds for cache to be valid
    data = cache.get(cache_key)  # returns None if no key-value pair
    if not data:
        users = User.objects.order_by('id')
        cache.set(cache_key, users)
    return HttpResponse(data)
