from django.db.models import Subquery, OuterRef
from movies.models import FilmWork, Genre, Person, GenreFilmWork, PersonFilmWork
from django.db import connection, reset_queries
from django.db.models import Count

from django.db.models import Prefetch


#  python manage.py runscript prefetch_related-01


def run():
    reset_queries()
    # queryset = FilmWork.objects.all()
    # queryset = FilmWork.objects.prefetch_related("genres", "persons").all()
    # queryset = FilmWork.objects.prefetch_related(
    #     "genrefilmwork", "personfilmwork"
    # ).all()

    queryset = FilmWork.objects.prefetch_related(
        Prefetch(
            "genrefilmwork", queryset=GenreFilmWork.objects.select_related("genre")
        ),
        Prefetch(
            "personfilmwork", queryset=PersonFilmWork.objects.select_related("person")
        ),
    )

    # Iterate through the queryset to access movie data along with genres
    for movie in queryset:
        print("Movie:", movie.title)
        for genre in movie.genres.all():
            print("Genre:", genre.name)

        for person_filmwork in movie.personfilmwork.all():
            print(
                "Person:",
                person_filmwork.person.full_name,
                "Role:",
                person_filmwork.role,
            )

    # print(connection.query)
    print(f"connection.queries {len(connection.queries)}")
