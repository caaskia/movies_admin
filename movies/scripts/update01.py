from django.db.models import Subquery, OuterRef
from movies.models import FilmWork, PersonFilmWork, Person
from django.db import connection, reset_queries


def run():
    try:
        # Subquery to filter PersonFilmWork objects based on the full_name field
        person_ids = Person.objects.filter(full_name="Samuli Torssonen").values("id")
        film_work_ids = PersonFilmWork.objects.filter(
            person_id__in=Subquery(person_ids)
        ).values("film_work_id")

        # Query FilmWork objects based on the filtered PersonFilmWork objects
        need_to_increase_rating = FilmWork.objects.filter(
            id__in=Subquery(film_work_ids)
        )
    except FilmWork.DoesNotExist as e:
        print("FilmWork matching query does not exist.")

    print(f"connection.queries {len(connection.queries)}")
