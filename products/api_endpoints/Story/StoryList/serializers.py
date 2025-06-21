from rest_framework import serializers
from products.models import Story

class StoryListSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Story
        fields = (
            'id',
            'title',
            'product',
            'image'
        )
        read_only_fields = ['id']


class StoryRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = (
            'id',
            'title',
            'product',
            'image',
            'created_at',
            'updated_at'
        )
        read_only_fields = ['id', 'created_at', 'updated_at']