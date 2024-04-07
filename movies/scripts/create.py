from django.db.models import Subquery, OuterRef
from movies.models import FilmWork, Genre, Person, PersonFilmWork
from django.db import connection, reset_queries


def run():
    reset_queries()

    try:
        # philosophical = Genre.objects.create(name="Philosophical")
        # philosophical.save()

        science_fiction = Genre()
        science_fiction.name = "Science fiction"
        science_fiction.description = "Advanced science and technology, space exploration, time travel, parallel universes, and extraterrestrial life."
        science_fiction.save()
    except Exception as e:
        print(f"Error creating genre: {e}")

    print(f"connection.queries {len(connection.queries)}")
