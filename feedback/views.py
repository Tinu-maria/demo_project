from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from feedback.models import Profile
from feedback.forms import FeedbackForm, RegistrationForm, LoginForm, ProfileForm
from django.contrib.auth.models import User
import logging
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.utils.decorators import method_decorator
from feedback.decorators import signin_required
from django.core.paginator import Paginator
from django.db.models import F, Value, CharField, Sum
from django.db.models.functions import Concat


class RegisterView(View):
    def get(self,request,*args,**kwargs):
        form = RegistrationForm()
        return render(request,"feedback/registration.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect("signin")
        
class LoginView(View):
    def get(self,request,*args,**kwargs):
        form = LoginForm()
        return render(request,"feedback/login.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user=authenticate(request, username=username, password=password)
            if user:
                # request.session['username'] = username
                login(request,user)
                return redirect('feedback')
            else:
                messages.error(request, "Invalid credentials")
                return redirect('signin')

class LogoutView(View):
    def get(self,request,*args,**kwargs):
        # if 'username' in request.session:
        #     request.session.flush()
        logout(request)
        return redirect("signin")    

@method_decorator(signin_required, name="dispatch")
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
    name1 = User.objects.annotate(full_name = Concat(F('first_name'), Value(' '), F('last_name'), output_field=CharField()))
    for name in name1:
        print(name.full_name)
    # name1 = User.objects.aggregate(full_name = Sum(F('first_name') + F('last_name'), output_field=CharField()))
    # print(name1['full_name'])

    log.info("Message for information")
    log.warning("Message for warning")
    log.error("Message for error")
    log.critical("Message for critical error")

    return render(request, 'feedback/index.html')

def pagination(request):
    # if 'username' in request.session:
    user = User.objects.all()
    p = Paginator(user,1)
    # p = Paginator(list_of_objects, no_of_objects_per_page)
    page_num = request.GET.get('page', 1)
    page = p.page(page_num)
    print(page_num)
    context = {'user' : page}
    return render(request, 'feedback/page.html', context)
    # return redirect("signin")  

@method_decorator(signin_required, name="dispatch")
class UserProfileAdd(TemplateView):
    template_name = "feedback/adduserprofile.html"

    def get(self, request, *args, **kwargs):
        form = ProfileForm()
        return render(request, 'feedback/adduserprofile.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            #for multiple fiile upload
            files = request.FILES.getlist('files')
            for file in files:
                new_file = Profile.objects.create(image=file)
                # new_file = Profile(image=file)
                new_file.save() 
                #for multiple fiile upload
            # form.save()
            return redirect('success')

class UserProfileView(ListView):
    model = Profile
    template_name = 'feedback/viewuserprofile.html'
    context_object_name = 'profiles'


def upload(request, *args, **kwargs):
    if (request.method == "POST"):
        files = request.FILES.getlist('files')
        for file in files:
            new_file = Profile(image=file)
            new_file.save()
        return render(request, 'feedback/viewuserprofile.html', {'files': new_file})
    else:
        return render(request, 'feedback/multipleupload.html')
