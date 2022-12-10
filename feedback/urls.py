from django.urls import path

from feedback.views import FeedbackFormView,SuccessView,index,RegisterView,LoginView,LogoutView, pagination

urlpatterns = [
    path("feedback/", FeedbackFormView.as_view(), name="feedback"),
    path("success/", SuccessView.as_view(), name="success"),
    path("index/", index, name="index"), 
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="signin"), 
    path("logout/", LogoutView.as_view(), name="signout"), 
    path("page/", pagination, name="page"), 
]
