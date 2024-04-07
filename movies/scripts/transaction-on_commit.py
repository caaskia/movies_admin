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

    from django.db import transaction

    with transaction.atomic():
        user = create_user()
        create_profile(user)
        add_random_profile_photo(user)
        transaction.on_commit(lambda: set_task_for_send_email_congratulations(user))

    print(f"connection.queries {len(connection.queries)}")
