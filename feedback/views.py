from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from feedback.forms import FeedbackForm, RegistrationForm, LoginForm
from django.contrib.auth.models import User
import os
import logging


class RegisterView(View):
    def get(self,request,*args,**kwargs):
        form = RegistrationForm()
        return render(request,"feedback/registration.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return render(request,"feedback/index.html")
        
class LoginView(View):
    def get(self,request,*args,**kwargs):
        form = LoginForm()
        return render(request,"feedback/login.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            return render(request,"feedback/index.html")

class FeedbackFormView(FormView):
    template_name = "feedback/feedback.html"
    form_class = FeedbackForm
    success_url = "/success/"

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = "feedback/success.html"
    

log = logging.getLogger('log')
def index(request):
    log.info("Message for information")
    log.warning("Message for warning")
    log.error("Message for error")
    log.critical("Message for critical error")
    return render(request, 'feedback/index.html')