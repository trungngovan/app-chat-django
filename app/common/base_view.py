from abc import abstractmethod
from typing import Union

from django.http import JsonResponse, HttpResponse
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import status


class APIResponseCode(object):
    FAILURE = (-1, 'General failure')  # General logic error
    SUCCESS = (0, 'Success')  # Successful response
    SERVER_ERROR = (1, 'Server error')  # Unexpected error during handling the request
    BAD_REQUEST = (2, 'Bad request')  # Error returned by DRF serializer
    NO_PERMISSION = (3, 'No permission')  # Error related to permissions
    NOT_FOUND = (4, 'Not found')  # Object not found
    ALREADY_EXISTS = (5, 'Already exists')  # Object already exists
    VALIDATION_ERROR = (6, 'Validation error')  # Error related to invalidated input
    INVALID_ACTION = (7, 'Invalid request')  # Invalid action (stateful)
    ACTION_DENIED = (8, 'Action denied')  # Invalid action (stateless)
    FILE_ERROR = (9, 'File error')  # Error related to file handling
    DB_ERROR = (10, 'Database error')  # Error related to database
    EXT_API_ERROR = (11, 'External API error')  # Error related to calling external API
    TIMEOUT = (12, 'Timeout')  # Timeout when handling a request
    EXPIRED = (13, 'Request expired')
    TOO_MANY_REQUEST = (14, 'Too many request')
    INSUFFICIENT_BALANCE = (15, 'Insufficient balance')
    REWARD_ALREADY_CLAIMED = (16, 'reward already claimed')
    OUT_OF_SLOT = (17, 'out of slot')
    ALREADY_SAVED = (18, 'already saved')
    MAX_RETRY_EXCEEDED = (19, 'max retries exceeded')
    OUT_OF_GIFT = (20, 'out of gift')

    @classmethod
    def is_success(cls, code):
        return code == cls.SUCCESS

    @classmethod
    def is_failure(cls, code):
        return code != cls.SUCCESS


class BaseAPIView(APIView):
    deserializer_class = None

    @staticmethod
    def _build_response_with_object(json_data):
        """
        :param dict | list | None json_data:
        :return:
        :rtype: dict
        """
        return {
            'data': json_data,
        }

    @classmethod
    def make_json_response(cls, response_code, json_data, status_code=200):
        """
        :param tuple response_code: core.views.APIResponseCode
        :param dict | list | None json_data: response data
        :param int status_code: rest_framework.status
        :return:
        :rtype: JsonResponse
        """
        json_response = cls._build_response_with_object(json_data)

        response = {
            'code': response_code[0],
            'msg': response_code[1],
        }
        response.update(json_response)

        return JsonResponse(response, status=status_code)

    def execute(self, request: Request, do_func, *args, **kwargs):

        try:
            valid_data, errors = self._parse_data(self.deserializer_class, self._get_raw_request_data(request))

            if errors:
                return self.make_json_response(APIResponseCode.BAD_REQUEST, errors, status.HTTP_400_BAD_REQUEST)

            response = do_func(request, valid_data, *args, **kwargs)

            return response
        except:

            return self.make_json_response(APIResponseCode.SERVER_ERROR, None, status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    def _parse_data(deserializer_class, data):
        if deserializer_class is None:
            return data, None

        serializer = deserializer_class(data=data)

        if serializer.is_valid():
            return serializer.validated_data, None

        return None, serializer.errors

    @staticmethod
    def _get_raw_request_data(request: Request):
        if request.method == 'GET':
            return request.query_params

        if request.method == 'POST':
            return request.data

        raise Exception('Method {} does not support get request raw data'.format(request.method))


class PostAPIView(BaseAPIView):
    def post(self, request: Request, *args, **kwargs):
        return self.execute(request, self.do_post, *args, **kwargs)

    @abstractmethod
    def do_post(self, request: Request, request_data: Union[dict, list], *args, **kwargs) -> HttpResponse:
        raise NotImplementedError('do_post must be implemented in subclass')


class GetAPIView(BaseAPIView):
    def get(self, request: Request, *args, **kwargs):
        return self.execute(request, self.do_get, *args, **kwargs)

    @abstractmethod
    def do_get(self, request: Request, request_data: Union[dict, list], *args, **kwargs) -> HttpResponse:
        raise NotImplementedError('do_get must be implemented in subclass')
