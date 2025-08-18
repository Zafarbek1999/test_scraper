from rest_framework.viewsets import ReadOnlyModelViewSet

from scraper.models import Job
from scraper.serializers import JobSerializer


class JobViewSet(ReadOnlyModelViewSet):
    queryset = Job.objects.order_by('-posted_at')
    serializer_class = JobSerializer
    search_fields = ['title', 'company', 'location', 'tags']

