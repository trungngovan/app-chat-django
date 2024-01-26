from app import models


def get_active_messages(message_id=None, room_id=None, author_id=None):
    return get_messages(message_id=message_id, room_id=room_id, author_id=author_id, is_deleted=False)


def get_messages_by_room_id(room_id):
    return get_active_messages(room_id=room_id)


def get_messages(message_id=None, room_id=None, author_id=None, is_deleted=None):
    query_set = models.Message.objects.all()

    if message_id is not None:
        query_set = query_set.filter(id=message_id)

    if room_id is not None:
        query_set = query_set.filter(room_id=room_id)

    if author_id is not None:
        query_set = models.Message.objects.select_related('author')
        query_set = query_set.filter(author_id=author_id)

    if is_deleted is not None:
        query_set = query_set.filter(is_deleted=is_deleted)

    return query_set


# def create_messages(room_dict):
#     new_room = models.Room()
#     new_room.__dict__.update(**room_dict)
#
#     new_room.websocket_url = '/rooms/%s/' % new_room.id
#     new_room.save()
#
#     return new_room
