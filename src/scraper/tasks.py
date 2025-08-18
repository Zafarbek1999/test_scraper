from django.conf import settings
from django.utils.dateparse import parse_datetime

from config import celery_app
from scraper.clients.remoteok import RemoteokClient
from scraper.models import Job


@celery_app.task(bind=True)
def fetch_remoteok_jobs(self):
    client = RemoteokClient()
    jobs = client.get_jobs()
    jobs_data = []
    for job in jobs[1:]:
        if not Job.objects.filter(external_id=int(job.get("id"))).exists():
            jobs_data.append(Job(
                external_id=int(job.get("id")),
                title=job.get("position"),
                company=job.get("company"),
                company_logo=job.get("company_logo") if job.get("company_logo") != "" else settings.DEFAULT_COMPANY_LOGO,
                url=job.get("url"),
                tags=", ".join(job.get("tags", [])),
                location=job.get("location"),
                salary_min=job.get("salary_min"),
                salary_max=job.get("salary_max"),
                posted_at=parse_datetime(job.get("date")),
            ))
    Job.objects.bulk_create(jobs_data, batch_size=300)
