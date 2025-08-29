# apps/pulses/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.pulses.models import Pulse
from apps.pulses.utils import broadcast_pulse


@receiver(post_save, sender=Pulse)
def pulse_created(sender, instance, created, **kwargs):
    if created:
        broadcast_pulse(instance)
