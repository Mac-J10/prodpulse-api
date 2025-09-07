from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Category, Product
from apps.users.permissions import IsVendor
from .serializers import CategorySerializer, ProductSerializer, ProductDetailSerializer
from apps.pulses.models import Pulse
from apps.pulses.serializers import PulseSerializer
from rest_framework.views import APIView
import httpx
from apps.analytics.models import ProductView
from django.db import models
from django.contrib.postgres.search import SearchQuery, SearchRank
from rest_framework.views import APIView

class ProductListView(APIView):
    def get(self, request):
        return Response({"message": "Product list placeholder"})

class ProductDetailView(APIView):
    def get(self, request, pk):
        return Response({"message": f"Product detail placeholder for {pk}"})

def retrieve(self, request, *args, **kwargs):
    resp = super().retrieve(request, *args, **kwargs)
    ProductView.objects.update_or_create(
        product_id=kwargs["pk"], defaults={"count": models.F("count") + 1}
    )
    return resp


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
    queryset = Product.objects.select_related("category").all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.query_params.get("search")
        if q:
            query = SearchQuery(q)
            qs = (
                qs.annotate(rank=SearchRank("search_vector", query))
                .filter(rank__gte=0.1)
                .order_by("-rank")
            )
        return qs

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsVendor()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ProductDetailSerializer
        return ProductSerializer

    @action(detail=True, methods=["get"], url_path="metrics")
    def list_metrics(self, request, pk=None):
        product = self.get_object()
        pulses = Pulse.objects.filter(product=product).order_by("-timestamp")
        page = self.paginate_queryset(pulses)
        serializer = PulseSerializer(page or pulses, many=True)
        return self.get_paginated_response(serializer.data)

    @action(detail=True, methods=["post"], url_path="metrics")
    def create_metric(self, request, pk=None):
        product = self.get_object()
        data = request.data.copy()
        data["product"] = product.id
        serializer = PulseSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
