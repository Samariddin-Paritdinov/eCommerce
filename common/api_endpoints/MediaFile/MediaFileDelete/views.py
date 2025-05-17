from rest_framework.generics import DestroyAPIView

from common.api_endpoints.MediaFile.MediaFileDelete.serializers import MediaFileDeleteSerializer
from common.models import MediaFile

class MediaFileDeleteAPIView(DestroyAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileDeleteSerializer
    lookup_field = 'id'