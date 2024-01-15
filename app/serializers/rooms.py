from rest_framework import serializers
from app import models


# Deserializer
class CreateRoomDeserializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, required=True)
    supervisor_id = serializers.IntegerField(required=False)


# Serializer
class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Room
        exclude = []

