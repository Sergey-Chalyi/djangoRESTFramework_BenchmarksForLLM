from django.db.models import Avg

from base import settings
from .models import Benchmark

from rest_framework.views import APIView
from rest_framework.exceptions import APIException

from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from datetime import datetime


class FeatureNotReadyException(APIException):
    status_code = 501
    default_detail = "This feature is not ready for live yet."
    default_code = "feature_not_ready"

class AverageResultsView(APIView):
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