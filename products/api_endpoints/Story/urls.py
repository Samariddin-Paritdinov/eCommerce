from django.urls import path

from products.api_endpoints.Story import (
    StoryCreateAPIView,
    StoryDeleteAPIView,
    StoryListAPIView,
    StoryRetrieveAPIView,
    StoryUpdateAPIView
)

urlpatterns = [
    path('create/', StoryCreateAPIView.as_view(), name='story-create'),
    path('read/', StoryListAPIView.as_view(), name='story-list'),
    path('read/<int:id>/', StoryRetrieveAPIView.as_view(), name='story-retrieve'),
    path('update/<int:id>/', StoryUpdateAPIView.as_view(), name='story-update'),
    path('delete/<int:id>/', StoryDeleteAPIView.as_view(), name='story-delete'),
]