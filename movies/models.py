import uuid
from django.db import models


class FilmWork(models.Model):
    id = models.UUIDField(primary_key=True)
    title = models.TextField()
    description = models.TextField(blank=True, null=True)
    creation_date = models.DateField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    type = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "content\".\"film_work"
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class Genre(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "content\".\"genre"
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Person(models.Model):
    id = models.UUIDField(primary_key=True)
    full_name = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "content\".\"person"
        verbose_name = 'Персона'
        verbose_name_plural = 'Персоны'


class PersonFilmWork(models.Model):
    id = models.UUIDField(primary_key=True)
    film_work = models.ForeignKey(FilmWork, on_delete=models.CASCADE, related_name='person_roles')
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    role = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"person_film_work"
        verbose_name = 'Персона фильма'
        verbose_name_plural = 'Персоны фильма'


class GenreFilmWork(models.Model):
    id = models.UUIDField(primary_key=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    film_work = models.ForeignKey(FilmWork, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"genre_film_work"
        verbose_name = 'Жанр фильма'
        verbose_name_plural = 'Жанры фильма'
