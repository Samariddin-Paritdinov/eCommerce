from rest_framework import serializers

from products.models import ProductVariant

class ProductVariantRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ['id', 'name', 'price', 'product', 'images', 'stock', 'color', 'size', 'is_active', 'created_at', 'updated_at']
        
