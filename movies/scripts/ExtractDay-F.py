import datetime

from django.db import models
from django.db.models.functions import ExtractDay, Abs
from movies.models import FilmWork, PersonFilmWork, Person
from django.db import connection, reset_queries
from django.db.models import F


def run():
    reset_queries()

    filmwork_qs = FilmWork.objects.all()
    expr = ExtractDay(
        models.ExpressionWrapper(
            datetime.datetime(2018, 11, 8) - F("creation_date"),
            output_field=models.DateField(),
        )
    )
    film = (
        filmwork_qs.annotate(delta=expr)
        .filter(delta__isnull=False)
        .annotate(abs_delta=Abs("delta"))
        .order_by("abs_delta")
        .first()
    )

    print(film)

    print(f"connection.queries {len(connection.queries)}")
