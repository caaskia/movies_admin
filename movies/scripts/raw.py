from django.db.models import Subquery, OuterRef
from movies.models import FilmWork, PersonFilmWork, Person
from django.db import connection, reset_queries


def run():
    reset_queries()

    try:
        film = FilmWork.objects.raw(
            'SELECT id, age(creation_date) AS age FROM "content"."film_work"'
        )[0]
        print(film.title, film.age)

        with connection.cursor() as cursor:
            cursor.execute(
                r"""UPDATE "content"."person" SET full_name = regexp_replace(full_name, '(\w+)(\W+)(\w+)', '\3\2\1');"""
            )

    except FilmWork.DoesNotExist as e:
        print("FilmWork matching query does not exist.")

    print(f"connection.queries {len(connection.queries)}")
