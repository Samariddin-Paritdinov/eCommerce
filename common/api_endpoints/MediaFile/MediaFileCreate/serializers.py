from rest_framework import serializers

from common.models import MediaFile

class MediaFileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = ['id', 'file']
        read_only_fields = ['id']


    # def validate_file(self, file):
    #     allowed_types = ['application/pdf', 'image/jpeg', 'image/png']
    #     if file.content_type not in allowed_types:
    #         raise serializers.ValidationError("Yuklanayotgan fayl turi ruxsat etilmagan.")
    #     return file
