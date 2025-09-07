from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

class NotificationViewSet(ViewSet):
    def list(self, request):
        return Response({"message": "Notifications endpoint stub"})