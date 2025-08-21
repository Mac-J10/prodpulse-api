from django.contrib.postgres.search import SearchVector
from django.db.models.signals import post_save
from .tasks import send_low_stock_alert
from django.dispatch import receiver
from .models import Product

@receiver(post_save, sender=Product)
def update_search_vector(sender, instance, **kwargs):
    instance.search_vector = (
        SearchVector('title', weight='A') +
        SearchVector('description', weight='B')
    )
    instance.save(update_fields=['search_vector'])

@receiver(post_save, sender=Product)
def low_stock_check(sender, instance, **kwargs):
    if instance.stock_qty < instance.low_stock_threshold:
        send_low_stock_alert.delay(instance.id)
