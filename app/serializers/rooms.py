from rest_framework import serializers
from app import models


# Deserializer
class CreateRoomDeserializer(serializers.Serializer):
    name_room = serializers.CharField(max_length=255, required=True)
    owner = serializers.CharField(required=True)
    password = serializers.CharField(max_length=8, required=True)


# Serializer
class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Room
        exclude = []
