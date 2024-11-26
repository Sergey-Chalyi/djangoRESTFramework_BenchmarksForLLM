from django.db.models import Avg

from base import settings
from .models import Benchmark

from rest_framework.views import APIView
from rest_framework.exceptions import APIException

from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from datetime import datetime


class FeatureNotReadyException(APIException):
    """
    Custom exception to be raised when a feature is not ready for live use.

    Attributes:
    status_code: The HTTP status code for this exception. Set to 501 (Not Implemented).
    default_detail: A human-readable description of the exception. Set to "This feature is not ready for live yet."
    default_code: A unique code for this exception. Set to "feature_not_ready".
    """
    status_code = 501
    default_detail = "This feature is not ready for live yet."
    default_code = "feature_not_ready"

class AverageResultsView(APIView):
    """
    A view that calculates and returns the average benchmarking results.

    This view is only accessible when the DEBUG setting is enabled. If DEBUG is False,
    a FeatureNotReadyException is raised.

    The view calculates the average values of token_count, time_to_first_token, time_per_output_token,
    and total_generation_time fields from the Benchmark model.

    Returns:
        A Response object containing the calculated averages.
    """

    def get(self, request):      
        if not settings.DEBUG:
            raise FeatureNotReadyException()
        
        averages = Benchmark.objects.aggregate(
            avg_token_count=Avg('token_count'),
            avg_time_to_first_token=Avg('time_to_first_token'),
            avg_time_per_output_token=Avg('time_per_output_token'),
            avg_total_generation_time=Avg('total_generation_time')
        )
        return Response(averages)


class AverageResultsByTimeView(APIView):
    """
    A view that calculates and returns the average benchmarking results within a specified time range.

    This view is only accessible when the DEBUG setting is enabled. If DEBUG is False,
    a FeatureNotReadyException is raised.

    Parameters:
    request (Request): The incoming request object.
    start_time (str): The start time of the time range in ISO 8601 format.
    end_time (str): The end time of the time range in ISO 8601 format.

    Returns:
    Response: A Response object containing the calculated averages if the time range is valid and results exist.
              If the DEBUG setting is False, a FeatureNotReadyException is raised.
              If the time range is invalid, a 400 Bad Request response is returned.
              If no benchmarking results are found in the specified time range, a 404 Not Found response is returned.
    """

    def get(self, request, start_time, end_time):      
        if not settings.DEBUG:
            raise FeatureNotReadyException()

        try:
            start_time = datetime.fromisoformat(start_time)
            end_time = datetime.fromisoformat(end_time)
        except ValueError:
            return Response({"error": "Invalid date format. Use ISO 8601 format."}, status=400)

        results = Benchmark.objects.filter(timestamp__range=(start_time, end_time))
        if not results.exists():
            raise NotFound("No benchmarking results found in the specified time range.")

        averages = results.aggregate(
            avg_token_count=Avg('token_count'),
            avg_time_to_first_token=Avg('time_to_first_token'),
            avg_time_per_output_token=Avg('time_per_output_token'),
            avg_total_generation_time=Avg('total_generation_time')
        )
        return Response(averages)