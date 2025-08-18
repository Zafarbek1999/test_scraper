import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('scraper')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    "sync_sms_template": {
        "task": "scraper.tasks.fetch_remoteok_jobs",
        "schedule": crontab(minute="*/5"),
    }
}

# Load task modules from all registered Django apps.
app.autodiscover_tasks()
