from rest_framework import serializers

from products.models import Story


class StoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = (
            'id',
            'title',
            'product',
            'image'
        )
        read_only_fields = ['id']
