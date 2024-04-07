import datetime

from django.db import models
from django.db.models.functions import ExtractDay, Abs
from movies.models import FilmWork, PersonFilmWork, Person
from django.db import connection, reset_queries
from django.db.models import Avg
from django.db.models import Q, F

import random
from django.db import transaction


def run():
    reset_queries()

    def get_rating_from_imdb(filmname):
        rating = random.randint(0, 6)
        if rating == 6:
            raise Exception("👿")
        return rating

    # Открытие новой транзакции
    @transaction.atomic
    def create_film_pack(filmname):
        # Начало транзакции
        # Падение любого участка кода приведёт к откату изменений
        add_film(filmname)
        add_actors(filmname)
        get_rating_from_imdb(filmname)
        add_genres(filmname)
        # Если блок завершился успешно, произойдёт коммит транзакции

    print(f"connection.queries {len(connection.queries)}")
