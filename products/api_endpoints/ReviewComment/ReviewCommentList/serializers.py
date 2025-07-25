from rest_framework import serializers

from products.models import Review, Comment, Product


class ProductForReviewCommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name"
        ]


class UserReviewsListSerializer(serializers.ModelSerializer):
    product = ProductForReviewCommentListSerializer()
    
    class Meta:
        model = Review
        fields = [
            "id",
            "product",
            "rating",
            "review",
            "created_at"
        ]


class UserCommentsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "id",
            "product",
            "text",
            "parent",
            "created_at"
        ]