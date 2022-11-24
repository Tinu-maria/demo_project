from django.urls import path

from feedback.views import FeedbackFormView, SuccessView, index

app_name = "feedback"

urlpatterns = [
    path("feedback/", FeedbackFormView.as_view(), name="feedback"),
    path("success/", SuccessView.as_view(), name="success"),
    path("index/", index, name="index"),  
]
