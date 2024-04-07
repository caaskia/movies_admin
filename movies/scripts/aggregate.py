import datetime

from django.db import models
from django.db.models.functions import ExtractDay, Abs
from movies.models import FilmWork, PersonFilmWork, Person
from django.db import connection, reset_queries
from django.db.models import Avg
from django.db.models import Q, F


def run():
    films = FilmWork.objects.filter(filmwork__role=PersonFilmWork.RoleChoices.ACTOR)
    #    films = FilmWork.objects.filter(filmwork__role=PersonFilmWork.RoleChoices.ACTOR.value)

    full_name = "Harrison Ford"
    films = FilmWork.objects.filter(filmwork__person__full_name=full_name)

    reset_queries()

    try:
        avr_rating = FilmWork.objects.filter(
            filmwork__person__full_name=full_name,
        ).aggregate(avr_rating=Avg("rating"))
        print(avr_rating)
    except Exception as e:
        print(e)

    print(f"connection.queries {len(connection.queries)}")
