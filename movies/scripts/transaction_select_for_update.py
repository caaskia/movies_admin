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

    persons_without_birthday = Person.objects.select_for_update().filter(
        birth_date__isnull=True
    )  # Создание ленивого QuerySet
    with transaction.atomic():  # Начало транзакции
        for (
            person
        ) in (
            persons_without_birthday
        ):  # Выполнение QuerySet: выполнена блокировка строк на уровне БД
            person.birth_date = get_birthday(person.full_name)
        ...

    # После завершения транзакции блокировка будет снята

    persons_without_birthday = Person.objects.select_for_update(of=("self",)).filter(
        birth_date__isnull=True
    )  # Создание ленивого QuerySet
    with transaction.atomic():
        for person in persons_without_birthday:
            person.birth_date = get_birthday(person.full_name)
        ...

    print(f"connection.queries {len(connection.queries)}")
