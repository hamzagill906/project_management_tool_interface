from celery.schedules import crontab
from django.conf import settings
from kombu import Exchange
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config", broker=settings.CELERY_BROKER_URL)
app.config_from_object("config.settings", namespace="CELERY")

app.conf.beat_schedule = {
    'check_due_dates': {
        'task': 'api.projects.tasks.check_due_dates',
        'schedule': crontab(minute=0, hour=0),  # Run once a day at midnight
    },
}
