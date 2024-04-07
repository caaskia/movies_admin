import datetime

from django.db.models import Subquery, OuterRef
from movies.models import FilmWork, Genre, Person, PersonFilmWork
from django.db import connection, reset_queries


def run():
    reset_queries()

    try:
        FilmWork.objects.create(
            title="Conan Varvar XI", creation_date=datetime.date.today(), rating=5
        )
    except Exception as e:
        print(f"Error creating genre: {e}")

    print(f"connection.queries {len(connection.queries)}")
