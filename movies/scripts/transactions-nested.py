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

    with transaction.atomic():
        some_code()
        try:
            with transaction.atomic():
                inner_code()
        except SmallError:
            logger.error("Произошла ошибка! Изменения inner_code не применены.")
        more_code()

    print(f"connection.queries {len(connection.queries)}")
