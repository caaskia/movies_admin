from django.core.paginator import Paginator
from django.db.models import Prefetch
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from movies.models import FilmWork, GenreFilmWork, PersonFilmWork
from movies.serializers import MovieSerializer


class MoviesListApi(APIView):

    def get(self, request):
        # Get all movies with genres and persons
        movies = FilmWork.objects.prefetch_related(
            Prefetch(
                "genrefilmwork", queryset=GenreFilmWork.objects.select_related("genre")
            ),
            Prefetch(
                "personfilmwork",
                queryset=PersonFilmWork.objects.select_related("person"),
            ),
        )

        # Paginate the queryset
        paginator = Paginator(movies, per_page=50)
        page_number = request.GET.get("page")
        # Check if the request is for the last page
        if page_number == "last":
            page_number = paginator.num_pages  # Set page_number to the last page number

        page_obj = paginator.get_page(page_number)

        # Get persons queryset from page_obj

        # Serialize the paginated queryset
        serializer = MovieSerializer(page_obj, many=True)

        # Construct the response data
        response_data = {
            "count": paginator.count,
            "total_pages": paginator.num_pages,
            "prev": (
                page_obj.previous_page_number() if page_obj.has_previous() else None
            ),
            "next": page_obj.next_page_number() if page_obj.has_next() else None,
            "results": serializer.data,
        }

        return Response(response_data)


class MoviesDetailApi(APIView):

    def get(self, request, pk):
        try:
            movie = FilmWork.objects.get(pk=pk)
        except FilmWork.DoesNotExist:
            return Response(
                {"error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = MovieSerializer(movie)
        return Response(serializer.data)
