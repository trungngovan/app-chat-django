import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from app.models import Room, Message, User
from app import services


class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.roomGroupName = None
        self.room_name = None

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_slug']
        self.roomGroupName = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.roomGroupName,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        content = text_data_json["message"]
        author = text_data_json["author"]
        room_id = text_data_json["room_id"]

        await self.save_message(content, author, room_id)

        await self.channel_layer.group_send(
            self.roomGroupName, {
                "type": "sendMessage",
                "content": content,
                "author": author,
                "room_id": room_id,
            }
        )

    async def sendMessage(self, event):
        content = event["content"]
        author = event["author"]
        room_id = event["room_id"]
        await self.send(text_data=json.dumps({"content": content, "author": author, "room_id": room_id}))

    @sync_to_async
    def save_message(self, content, username, room_id):
        author = User.objects.get(username=username)
        room = Room.objects.get(id=room_id)
        Message.objects.create(author=author, room=room, content=content)
