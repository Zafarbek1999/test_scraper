from rest_framework.routers import DefaultRouter

from scraper.views import JobViewSet

router = DefaultRouter()
router.register(r'jobs', JobViewSet)

urlpatterns = []

urlpatterns += router.urls
