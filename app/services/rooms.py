from app import db_managers, serializers
# from app.common.response import APIResponseCode


def get_rooms():
    rooms = db_managers.get_active_rooms()

    return serializers.RoomSerializer(rooms, many=True).data


def get_room_by_slug(slug):
    rooms = db_managers.get_room_by_slug(slug)

    return serializers.RoomSerializer(rooms).data
