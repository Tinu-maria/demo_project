from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from demo_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("user/register", views.UserRegistrationView, basename="register")
router.register('user/profile', views.UserProfileView, basename="profile")

urlpatterns = [
                  path('token', TokenObtainPairView.as_view()),
                  path('token/refresh', TokenRefreshView.as_view()),
                  path('student', views.StudentView.as_view()),
                  path('student/<int:id>/', views.StudentDetailView.as_view()),
                  path('generic/profile/', views.GenericProfileView.as_view()),
                  path('generic/<int:id>/', views.GenericView.as_view()),
                  path('profile/', views.ProfileListView.as_view(), name='profile-get'),
                  path('student/', views.StudentListView.as_view(), name='student-get'),
              ] + router.urls
