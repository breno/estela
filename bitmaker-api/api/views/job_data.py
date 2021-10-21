import json

from bson.json_util import loads
from ***REMOVED***.conf import settings
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, mixins
from rest_framework.response import Response
from rest_framework.utils.urls import replace_query_param

from api import errors
from api.mixins import BaseViewSet
from core.mongo import get_client


class JobDataViewSet(
    BaseViewSet,
    mixins.ListModelMixin,
):
    MAX_PAGINATION_SIZE = 100
    MIN_PAGINATION_SIZE = 1
    DEFAULT_PAGINATION_SIZE = 50
    JOB_DATA_TYPES = ["items", "requests"]

    def get_parameters(self, request):
        page = int(request.query_params.get("page", 1))
        data_type = request.query_params.get("type", "items")
        page_size = int(
            request.query_params.get("page_size", self.DEFAULT_PAGINATION_SIZE)
        )
        return page, data_type, page_size

    def get_paginated_link(self, page_number):
        if page_number < 1:
            return None
        url = self.request.build_absolute_uri()
        return replace_query_param(url, "page", page_number)

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: openapi.Response(
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    required=["count", "result"],
                    properties={
                        "count": openapi.Schema(
                            type=openapi.TYPE_NUMBER,
                        ),
                        "previous": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            format=openapi.FORMAT_URI,
                            x_nullable=True,
                        ),
                        "next": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            format=openapi.FORMAT_URI,
                            x_nullable=True,
                        ),
                        "results": openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Items(type=openapi.TYPE_OBJECT),
                        ),
                    },
                ),
                description="",
            ),
        },
        manual_parameters=[
            openapi.Parameter(
                "type",
                openapi.IN_QUERY,
                description="Spider job data type.",
                type=openapi.TYPE_STRING,
                required=False,
            ),
        ],
    )
    def list(self, request, *args, **kwargs):
        page, data_type, page_size = self.get_parameters(request)
        if page_size > self.MAX_PAGINATION_SIZE or page_size < self.MIN_PAGINATION_SIZE:
            return Response(
                {"error": errors.INVALID_PAGE_SIZE}, status=status.HTTP_400_BAD_REQUEST
            )
        if page_size < 1:
            return Response(
                {"error": errors.INVALID_PAGE_NUMBER},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if data_type not in self.JOB_DATA_TYPES:
            return Response(
                {"error": errors.INVALID_JOB_DATA_TYPE},
                status=status.HTTP_400_BAD_REQUEST,
            )
        client = get_client(settings.MONGO_CONNECTION)
        if not client:
            return Response(
                {"error": errors.UNABLE_CONNECT_DB},
                status=status.HTTP_404_NOT_FOUND,
            )
        job_collection_name = "{}-{}-job_{}".format(
            kwargs["sid"], kwargs["jid"], data_type
        )
        job_collection = client[kwargs["pid"]][job_collection_name]
        result = job_collection.find().skip(page_size * (page - 1)).limit(page_size)
        result = loads(json.dumps(list(result), default=str))
        count = job_collection.estimated_document_count()

        return Response(
            {
                "count": count,
                "previous": self.get_paginated_link(page - 1),
                "next": self.get_paginated_link(page + 1)
                if page * page_size < count
                else None,
                "results": result,
            }
        )