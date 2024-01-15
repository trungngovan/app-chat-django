from app import models


def get_active_rooms(room_id=None, slug=None):
    return get_rooms(room_id=room_id, slug=slug, is_deleted=False)


def get_room_by_slug(slug):
    return get_active_rooms(slug=slug).first()


def get_rooms(room_id=None, slug=None, is_deleted=None):
    query_set = models.Room.objects.all()

    if room_id is not None:
        query_set = query_set.filter(id=room_id)

    if slug is not None:
        query_set = query_set.filter(slug=slug)

    if is_deleted is not None:
        query_set = query_set.filter(is_deleted=is_deleted)

    return query_set


def create_room(room_dict):
    new_room = models.Room()
    new_room.__dict__.update(**room_dict)

    new_room.websocket_url = '/rooms/%s/' % new_room.id
    new_room.save()

    return new_room
