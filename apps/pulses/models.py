from django.db import models


class Pulse(models.Model):
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="pulses"
    )
    timestamp = models.DateTimeField(db_index=True)
    value = models.DecimalField(max_digits=12, decimal_places=4)
    unit = models.CharField(max_length=20, default="unit")

    class Meta:
        ordering = ["-timestamp"]
        indexes = [
            models.Index(fields=["product", "timestamp"]),
        ]

    def __str__(self):
        ts = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        return f"Pulse for {self.product.sku} at {ts}: {self.value} {self.unit}"
