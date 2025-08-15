from rest_framework import serializers
from .models import Pulse

class PulseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pulse
        fields = ['id', 'product', 'timestamp', 'value', 'unit']
        read_only_fields = ['id', 'timestamp']

    def validate_value(self, value):
        if value < 0:
            raise serializers.ValidationError("Pulse value cannot be negative.")
        return value