from rest_framework import serializers
from app import models
from django.contrib.auth.models import User


# Serializer
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        models = User
        # fields = ('username', 'email', 'id')
        exclude = []


class MessageSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer()

    class Meta:
        model = models.Message
        exclude = ["is_deleted","created_at", "updated_at"]

