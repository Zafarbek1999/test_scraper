from django.core.management.base import BaseCommand

from src.scraper.tasks import fetch_remoteok_jobs


class Command(BaseCommand):
    help = "Scrape jobs from RemoteOK"

    def handle(self, *args, **kwargs):
        fetch_remoteok_jobs()
        self.stdout.write(self.style.SUCCESS(f"Jobs scraped successfully!"))
