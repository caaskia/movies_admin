import datetime

from django.db.models import Q
from django.db import connection, reset_queries
from movies.models import FilmWork


def run():

    reset_queries()

    try:
        # dataset = FilmWork.objects.filter(Q(rating__gte=8))

        dataset = FilmWork.objects.filter(
            Q(rating__gte=8)
            | Q(creation_date__gte=datetime.date(year=2020, month=1, day=1))
        )
    except FilmWork.DoesNotExist as e:
        print("FilmWork matching query does not exist.")

    for filmwork in dataset:
        print(filmwork.title)

    print(f"connection.queries {len(connection.queries)}")
