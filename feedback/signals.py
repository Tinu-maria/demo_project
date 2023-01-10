from django.db.models import signals
from django.dispatch import receiver
from feedback.models import Feedback


@receiver(signals.post_save, sender=Feedback)
def create_user(sender, instance, created, **kwargs):
    print("Feedback created")


@receiver(signals.pre_save, sender=Feedback)
def check_user(sender, instance, **kwargs):
    if not instance.message:
        instance.message = "Good feedback"
