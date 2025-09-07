from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

class OrderViewSet(ViewSet):
    def list(self, request):
        return Response({"message": "Orders endpoint stub"})