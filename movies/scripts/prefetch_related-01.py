from django.db.models import Subquery, OuterRef
from movies.models import FilmWork, PersonFilmWork, Person
from django.db import connection, reset_queries
from django.db.models import Count


def run():
    actors = Person.objects.all()

    #    actors = Person.objects.filter(
    #        personfilmwork__role=PersonFilmWork.RoleChoices.ACTOR
    #    ).prefetch_related("personfilmwork__film_work")
    #    for actor in actors:
    #        print(actor.full_name, actor.personfilmwork.count())

    try:
        print(
            *Person.objects.filter(
                personfilmwork__role=PersonFilmWork.RoleChoices.ACTOR
            )
            .annotate(count=Count("personfilmwork__film_work"))
            .values_list("full_name", "count"),
            sep="\n",
        )
    except Exception as e:
        print(f"Error: {e}")

    print(f"connection.queries {len(connection.queries)}")
