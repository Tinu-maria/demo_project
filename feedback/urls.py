from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from feedback.views import FeedbackFormView,SuccessView,index,RegisterView,LoginView,LogoutView,pagination,UserProfileAdd,upload,UserProfileView

urlpatterns = [
    path("feedback/", FeedbackFormView.as_view(), name="feedback"),
    path("success/", SuccessView.as_view(), name="success"),
    path("index/", index, name="index"), 
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="signin"), 
    path("logout/", LogoutView.as_view(), name="signout"), 
    path("page/", pagination, name="page"), 
    path("profile/add", UserProfileAdd.as_view(), name="addprofile"), 
    path("profile/view", UserProfileView.as_view(), name="viewprofile"), 

    path("profile/multiple", upload, name="multipleprofile"), 
    # path("profile/multipleupload", upload_multiple_files, name="multipleupload"), 
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
