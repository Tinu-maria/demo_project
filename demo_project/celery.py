import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo_project.settings")
# we use .setdefault() of os.environ to assure that your Django project’s settings.py module is accessible through
# the "DJANGO_SETTINGS_MODULE" key

app = Celery("demo_project")
# we create the Celery application instance and provide the name of the main module as an argument

app.config_from_object("django.conf:settings", namespace="CELERY")
# we define the Django settings file as the configuration file for Celery and provide a namespace, "CELERY"  

app.autodiscover_tasks()
# we tell our Celery application instance to automatically find all tasks in each app of our Django project


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))  # prints all metadata about the request when task is received


