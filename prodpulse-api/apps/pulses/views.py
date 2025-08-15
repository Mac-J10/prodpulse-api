from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.users.permissions import IsAdminOrVendor

from .models import Pulse
from .serializers import PulseSerializer

class PulseViewSet(viewsets.ModelViewSet):
    queryset = Pulse.objects.select_related('product').all()
    serializer_class = PulseSerializer
    permission_classes = [IsAuthenticated, IsAdminOrVendor]