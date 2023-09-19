import os
from celery import Celery
from celery.signals import worker_process_init
from opentelemetry.instrumentation.celery import CeleryInstrumentor

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

# Initialize the Celery app
app = Celery("core")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

# Initialize OpenTelemetry Celery instrumentation
CeleryInstrumentor().instrument()
# Define a function for worker process initialization
def initialize_worker(sender=None, **kwargs):
    # Add your initialization code here
    print("Worker process initialized!")
    # You can access the Celery app instance with 'app'

# Connect the worker_process_init signal to the initialization function
worker_process_init.connect(initialize_worker)
