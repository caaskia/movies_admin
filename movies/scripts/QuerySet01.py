from django.db.models import Subquery, OuterRef
from movies.models import FilmWork, PersonFilmWork, Person
from django.db import connection, reset_queries
from django.db.models import Count


def run():
    try:
        print(
            *Person.objects.filter(film_works__role=PersonFilmWork.RoleChoices.ACTOR)
            .annotate(count=Count("filmwork"))
            .values_list("full_name", "count"),
            sep="\n",
        )
    except Exception as e:
        print(f"Error: {e}")

    print(f"connection.queries {len(connection.queries)}")
