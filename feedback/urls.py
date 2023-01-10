from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from feedback import views

urlpatterns = [
                  path("feedback/", views.FeedbackFormView.as_view(), name="feedback"),
                  path("success/", views.SuccessView.as_view(), name="success"),
                  path("index/", views.index, name="index"),
                  path("register/", views.RegisterView.as_view(), name="register"),
                  path("login/", views.LoginView.as_view(), name="signin"),
                  path("logout/", views.LogoutView.as_view(), name="signout"),
                  path("page/", views.pagination, name="page"),
                  path("profile/add", views.UserProfileAdd.as_view(), name="addprofile"),
                  path("profile/view", views.UserProfileView.as_view(), name="viewprofile"),
                  path("cache", views.cache_view, name="cache"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
