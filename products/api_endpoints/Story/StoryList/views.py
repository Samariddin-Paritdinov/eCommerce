from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from products.models import Story
from products.api_endpoints.Story.StoryList.serializers import StoryListSerializer, StoryRetrieveSerializer


class StoryListAPIView(ListAPIView):
    queryset = Story.objects.filter(is_active=True).order_by("-created_at")
    serializer_class = StoryListSerializer
    permission_classes = [IsAuthenticated]


class StoryRetrieveAPIView(RetrieveAPIView):
    queryset = Story.objects.filter(is_active=True).order_by("-created_at")
    serializer_class = StoryRetrieveSerializer
    permission_classes = [IsAuthenticated]

    lookup_field = 'id' 