from django.db.models import Subquery, OuterRef
from movies.models import FilmWork, Genre, Person, PersonFilmWork
from django.db import connection, reset_queries


def run():
    reset_queries()

    try:
        persons_without_birthday = Person.objects.filter(birth_date__isnull=True)

        for person in persons_without_birthday:
            person.birth_date = get_birthday(person.full_name)

        Person.objects.bulk_update(persons_without_birthday, fields=["birth_date"])
    except Exception as e:
        print(f"Error creating genre: {e}")

    print(f"connection.queries {len(connection.queries)}")
