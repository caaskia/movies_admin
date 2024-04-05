# python manage.py runscript connection01

from django.db import connection
from movies.models import Genre

def run():
    genres = Genre.objects.all()
    qry = connection.queries  # []
    print(qry)
    print(genres)
    print(connection.queries)  # [{'sql': 'SELECT "content"."genre"."created_at", "content"."genre"."updated_at", "content"."genre"."id", "content"."genre"."name", "content"."genre"."description" FROM "content"."genre" LIMIT 21', 'time': '0.005'}]
    print(len(connection.queries))  # 1


