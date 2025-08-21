from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.users.permissions import IsAdminOrVendor

from .models import Pulse
from .serializers import PulseSerializer
import httpx
from rest_framework.views import APIView
from rest_framework.response import Response

class ExternalMetricIngestView(APIView):
    permission_classes = [IsAuthenticated]

    async def post(self, request, product_id):
        async with httpx.AsyncClient() as client:
            response = await client.get(f"https://external.api/metrics/{product_id}")
            data = response.json()

        # Save to DB (sync ORM wrapped in async)
        from asgiref.sync import sync_to_async
        await sync_to_async(Pulse.objects.create)(
            product_id=product_id,
            timestamp=data['timestamp'],
            value=data['value'],
            unit=data.get('unit', 'unit')
        )

        return Response({"detail": "Metric ingested"}, status=201)

class PulseViewSet(viewsets.ModelViewSet):
    queryset = Pulse.objects.select_related('product').all()
    serializer_class = PulseSerializer
    permission_classes = [IsAuthenticated, IsAdminOrVendor]