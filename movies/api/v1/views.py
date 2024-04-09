from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView
from rest_framework import pagination, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from movies.models import FilmWork
from movies.serializers import MovieSerializer

class MoviesApiMixin:
    model = FilmWork
    http_method_names = ["get"]

    def get_queryset(self):
        return self.model.objects.all()

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)

class MoviesListApi(APIView):
    def get(self, request):
        # Assuming you have queryset containing all movies
        movies = FilmWork.objects.all()

        # Paginate the queryset
        paginator = Paginator(movies, per_page=50)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # Serialize the paginated queryset
        serializer = MovieSerializer(page_obj, many=True)

        # Construct the response data
        response_data = {
            'count': paginator.count,
            'total_pages': paginator.num_pages,
            'prev': page_obj.previous_page_number() if page_obj.has_previous() else None,
            'next': page_obj.next_page_number() if page_obj.has_next() else None,
            'results': serializer.data
        }

        return Response(response_data)



class MoviesDetailApi(APIView):
    def get(self, request, pk):
        try:
            movie = FilmWork.objects.get(pk=pk)
        except FilmWork.DoesNotExist:
            return Response({"error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = MovieSerializer(movie)
        return Response(serializer.data)


