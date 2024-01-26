from app import db_managers, serializers
# from app.common.response import APIResponseCode


def get_messages():
    messages = db_managers.get_active_messages()
    return serializers.MessageSerializer(messages, many=True).data


def get_messages_by_room_id(room_id):
    queryset = db_managers.get_messages_by_room_id(room_id)
    messages = []

    for message in queryset:
        messages.append({
            'id': message.id,
            'content': message.content,
            'author_id': message.author.id,
            'author': message.author.username,
            'room': message.room.id,
        })

    return messages
