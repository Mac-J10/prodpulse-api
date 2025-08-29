from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Product


@shared_task
def send_low_stock_alert(product_id):
    prod = Product.objects.get(pk=product_id)
    subject = f"Low stock alert: {prod.title}"
    body = f"{prod.title} (SKU: {prod.sku}) has only {prod.stock_qty} items left."
    send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [settings.ADMIN_EMAIL])
