from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
import os
import logging

from feedback.forms import FeedbackForm


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