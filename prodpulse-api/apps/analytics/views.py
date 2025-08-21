from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .services.stripe_service import get_monthly_usage
from apps.orders.models import Order  # Adjust the import path as needed
from django.db import models
from django.db.models import Sum

from apps.orders.models import Order

@api_view(['GET'])
@permission_classes([IsAdminUser])
def stripe_usage(request):
    data = get_monthly_usage()
    return Response(data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def sales_estimate(request):
    data = Order.objects.aggregate(total_sales=Sum('total_amount'))
    return Response(data)

