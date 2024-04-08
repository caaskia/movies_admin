from django.http import JsonResponse
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView
from rest_framework import pagination, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from movies.models import FilmWork
from movies.serializers import MovieSerializer

# curl http://127.0.0.1:8000/api/v1/movies/movies?page=2
# curl http://127.0.0.1:8000/api/v1/movies/78efe505-6ef8-41f7-88ef-15840be2e680
# curl http:////127.0.0.1:8000/api/v1/movies/wrongUuid/

class MoviesApiMixin:
    model = FilmWork
    http_method_names = ["get"]

    def get_queryset(self):
        return self.model.objects.all()

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)


class CustomPagination(pagination.PageNumberPagination):
    page_size = 50


class MoviesListApi(MoviesApiMixin, generics.ListAPIView):
    serializer_class = MovieSerializer
    pagination_class = CustomPagination  # Assuming you have defined CustomPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        # Your custom queryset logic here
        return queryset


class MoviesDetailApi(APIView):
    def get(self, request, pk):
        try:
            movie = FilmWork.objects.get(pk=pk)
        except FilmWork.DoesNotExist:
            return Response({"error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = MovieSerializer(movie)
        return Response(serializer.data)


