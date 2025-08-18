from django.conf import settings
from django.db import models


class Job(models.Model):
    external_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    company_logo = models.URLField(max_length=500, default=settings.DEFAULT_COMPANY_LOGO)
    url = models.URLField(max_length=500,)
    tags = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    salary_min = models.DecimalField(max_digits=10, decimal_places=2)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2)
    posted_at = models.DateTimeField(null=True, blank=True)
    scraped_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company}"
