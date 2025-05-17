from rest_framework import serializers

from products.models import Product

class ProductRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'brand', 'slug', 'category', 'is_active', 'created_at', 'updated_at']
        