from django.db import models

# Creating my models.
from django.conf import settings
from django.db import models


class Product(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="products"
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.owner.username})"


class Pulse(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="pulses"
    )
    metric = models.CharField(max_length=100)
    value = models.FloatField()
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ["-timestamp"]
        indexes = [
            models.Index(fields=["timestamp"]),
        ]

    def __str__(self):
        return f"{self.metric}: {self.value} @ {self.timestamp}"
