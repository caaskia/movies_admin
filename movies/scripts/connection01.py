# python manage.py runscript connection01

from django.db import connection, reset_queries
from movies.models import FilmWork, Genre, GenreFilmWork


def run():
    # genres = Genre.objects.all()
    # qry = connection.queries  # []
    # print(qry)
    # print(genres)
    # print(connection.queries)  # [{'sql': 'SELECT "content"."genre"."created_at", "content"."genre"."updated_at", "content"."genre"."id", "content"."genre"."name", "content"."genre"."description" FROM "content"."genre" LIMIT 21', 'time': '0.005'}]
    # print(len(connection.queries))  # 1

    reset_queries()

    # filmworks_genres = GenreFilmWork.objects.all()[:3]
    # for filmwork_genre in filmworks_genres:
    #     print(filmwork_genre.filmwork.title, filmwork_genre.genre.name)
    # print(f"connection.queries {len(connection.queries)}")  # 1

    # filmworks_genres = GenreFilmWork.objects.all().select_related('film_work', 'genre')[:3]
    #
    # # Iterate over the queryset
    # for filmwork_genre in filmworks_genres:
    #     print(filmwork_genre.film_work)
    #     print(filmwork_genre.genre)

    # try:
    #     star_wars_films = FilmWork.objects.prefetch_related('genres', 'persons').filter(title__icontains='Star Wars')[
    #                       :10]
    #     for filmwork in star_wars_films:
    #         print(filmwork.genres.all())
    #         print(filmwork.persons.all())
    # except FilmWork.DoesNotExist as e:
    #     print("FilmWork matching query does not exist.")
    # except Exception as e:
    #     print(e)

    # all_genres = Genre.objects.all()
    # print(all_genres[:5])
    # print(all_genres[5:10])

    # star_wars_films = FilmWork.objects.prefetch_related('genres', 'persons').filter(title__icontains='Star Wars')[:10]
    # for filmwork in star_wars_films:
    #     print(filmwork.genres.all())
    #     print(filmwork.persons.filter(person__full_name='Robert'))

    FilmWork.objects.filter(genres__name="Western").count()

    # reset_queries()
    # len(FilmWork.objects.filter(genres__name='Western'))

    print(f"connection.queries {len(connection.queries)}")
