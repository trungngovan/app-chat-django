from django.contrib.auth.models import User
from django.db import models
from app.models import Room


# Create your models here.
class Message(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=2555)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    class Meta:
        db_table = "message"
