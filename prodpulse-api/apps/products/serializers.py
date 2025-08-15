from rest_framework import serializers
from .models import Category, Product
from apps.pulses.serializers import PulseSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )

    class Meta:
        model = Product
        fields = [
            'id', 'title', 'sku', 'description',
            'metadata', 'category', 'category_id',
            'created_at', 'updated_at'
        ]
    
class ProductDetailSerializer(ProductSerializer):
    metrics = serializers.SerializerMethodField()
    
    def get_metrics(self, obj):
        pulses = obj.pulses.order_by('-timestamp')[:20]
        return PulseSerializer(pulses, many=True).data
    
    class Meta(ProductSerializer.Meta):
        fields = ProductSerializer.Meta.fields + ['metrics']
