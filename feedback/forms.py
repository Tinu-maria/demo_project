from django import forms
from feedback.tasks import send_feedback_email_task
from django.contrib.auth.models import User
from feedback.models import Profile


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password"]

        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.TextInput(attrs={"class": "form-control"})
        }


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    email = forms.CharField(
        label="Email", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        label="Password", widget=forms.TextInput(attrs={"class": "form-control"})
    )


class FeedbackForm(forms.Form):
    email = forms.EmailField(
        label="Email Address", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    message = forms.CharField(
        label="Message", widget=forms.Textarea(attrs={"class": "form-control", "rows": 5})
    )

    def send_email(self):
        send_feedback_email_task.delay(
            self.cleaned_data["email"], self.cleaned_data["message"]
        )  # Using .delay() we can send a task message quickly to Celery

        # send_feedback_email_task(
        #     self.cleaned_data["email"],self.cleaned_data["message"]
        # ) 


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'title']
        widgets = {
            "title": forms.TextInput(attrs={"class":"form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control", "multiple": True}),
        }
