from django.db.models import Subquery, OuterRef
from movies.models import FilmWork, Genre, Person, PersonFilmWork
from django.db import connection, reset_queries


def run():
    reset_queries()

    try:
        Genre.objects.bulk_create(
            [Genre(name="Science fiction"), Genre(name="Philosophical")]
        )

        # batch_size
        # FilmWork.objects.bulk_create(large_filmworks_list, batch_size=500)
    except Exception as e:
        print(f"Error creating genre: {e}")

    print(f"connection.queries {len(connection.queries)}")
