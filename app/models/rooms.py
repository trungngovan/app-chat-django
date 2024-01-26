from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Room(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.SlugField(max_length=255)
    name_room = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=255)
    websocket_url = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_room

    class Meta:
        db_table = "room"
