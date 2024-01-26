from typing import Union
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.request import Request

from app import serializers
from app.common.base_view import PostAPIView, GetAPIView
from app.services import rooms as room_services, messages as message_services


class GetRoomsView(GetAPIView):
    deserializer_class = None
    permission_classes = ()

    def do_get(self, request: Request, request_data: Union[dict, list], *args, **kwargs) -> HttpResponse:
        rooms = room_services.get_rooms()

        return render(request, "room/rooms.html", {
            "rooms": rooms
        })


class CreateRoomView(PostAPIView):
    deserializer_class = serializers.CreateRoomDeserializer
    permission_classes = ()

    def do_post(self, request: Request, request_data: Union[dict, list], *args, **kwargs) -> HttpResponse:
        new_room = room_services.create_room(request_data)
        return redirect("rooms")


class GetRoomView(GetAPIView):
    deserializer_class = None
    permission_classes = ()

    def do_get(self, request: Request, request_data: Union[dict, list], *args, **kwargs) -> HttpResponse:
        slug = kwargs.get("slug")
        room = room_services.get_room_by_slug(slug)
        messages = message_services.get_messages_by_room_id(room["id"])
        return render(request, "room/room.html", {
            "slug": slug,
            "room": room,
            "messages": messages
        })
