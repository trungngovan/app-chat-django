from typing import Union
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.request import Request
from app.common.base_view import GetAPIView


class GetHomeView(GetAPIView):
    deserializer_class = None
    permission_classes = ()

    def do_get(self, request: Request, request_data: Union[dict, list], *args, **kwargs) -> HttpResponse:
        return render(request, "home.html")

