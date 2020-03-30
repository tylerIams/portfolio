from rest_framework import viewsets, permissions
from home.models import Announcement
from .serializers import AnnouncementSerializer

# Announcement Viewset
class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AnnouncementSerializer
