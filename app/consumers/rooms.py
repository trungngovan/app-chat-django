from channels.generic.websocket import AsyncWebsocketConsumer
from app.models import Room


class RoomConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room = None
        self.room_id = None

    def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room = Room.objects.get(id=self.room_id)

        if self.room.password != self.scope['user'].username:
            self.close()
            return

        self.room.users.add(self.scope['user'])

        # Thêm thông tin kênh WebSocket vào đối tượng Room
        self.room.websocket_url = self.channel_layer.routing.get_path('websocket_connect', self.channel_name)
        self.room.save()
        self.accept()

