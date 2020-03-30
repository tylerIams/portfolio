from rest_framework import routers
from .api import AnnouncementViewSet

router = routers.DefaultRouter()
router.register("api/announcement", AnnouncementViewSet, "announcement")

urlpatterns = router.urls
