from django.urls import path

from products.api_endpoints.ReviewComment import (
    ReviewCreateAPIView,
    CommentCreateAPIView,
    ReviewDeleteAPIView,
    CommentDeleteAPIView,
    UserReviewsListAPIView,
    UserCommentsListAPIView,
)

urlpatterns = [
    path('review/create/', ReviewCreateAPIView.as_view(), name='review-create'),
    path('review/delete/<int:pk>/', ReviewDeleteAPIView.as_view(), name='review-delete'),
    path('user-reviews/', UserReviewsListAPIView.as_view(), name='user-reviews-list'),
    path('comment/create/', CommentCreateAPIView.as_view(), name="comment-create"),
    path('comment/delete/<int:pk>/', CommentDeleteAPIView.as_view(), name="comment-delete"),
    path('user-comments/', UserCommentsListAPIView.as_view(), name='user-comments-list'),
]
