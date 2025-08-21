from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Category, Product
from apps.users.permissions import IsVendor
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    ProductDetailSerializer
)
from apps.pulses.models import Pulse
from apps.pulses.serializers import PulseSerializer
from rest_framework.views import APIView
import httpx

class ProductMetricsView(APIView):
    async def get(self, request, product_id):
        async with httpx.AsyncClient() as client:
            response = await client.get(f"https://external.api/metrics/{product_id}")
        data = response.json()
        return Response(data)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('category').all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsVendor()]
        return [IsAuthenticated()]


    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductDetailSerializer
        return ProductSerializer

    @action(detail=True, methods=['get'], url_path='metrics')
    def list_metrics(self, request, pk=None):
        product = self.get_object()
        pulses = Pulse.objects.filter(product=product).order_by('-timestamp')
        page = self.paginate_queryset(pulses)
        serializer = PulseSerializer(page or pulses, many=True)
        return self.get_paginated_response(serializer.data)

    @action(detail=True, methods=['post'], url_path='metrics')
    def create_metric(self, request, pk=None):
        product = self.get_object()
        data = request.data.copy()
        data['product'] = product.id
        serializer = PulseSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)