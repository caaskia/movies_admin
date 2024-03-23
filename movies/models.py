from django.core.validators import MinValueValidator, MaxValueValidator

from django.db import models
import uuid


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class FilmWork(TimeStampedMixin, UUIDMixin):
    class TypeChoices(models.TextChoices):
        MOVIE = 'movie', 'Movie'
        TV_SHOW = 'tv_show', 'TV Show'

    title = models.TextField()
    description = models.TextField(blank=True, null=True)
    creation_date = models.DateField(blank=True, null=True)
    rating = models.FloatField('rating', blank=True,
                               validators=[MinValueValidator(0),
                                           MaxValueValidator(100)])
    type = models.CharField(max_length=8, choices=TypeChoices.choices)

    class Meta:
        db_table = "content\".\"film_work"
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.title


class Genre(TimeStampedMixin, UUIDMixin):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Meta:
        db_table = "content\".\"genre"
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Person(TimeStampedMixin, UUIDMixin):
    full_name = models.TextField()

    class Meta:
        db_table = "content\".\"person"
        verbose_name = 'Персона'
        verbose_name_plural = 'Персоны'

    def __str__(self):
        return self.full_name


class PersonFilmWork(TimeStampedMixin, UUIDMixin):
    class RoleChoices(models.TextChoices):
        ACTOR = 'actor', 'Actor'
        PRODUCER = 'producer', 'Producer'
        DIRECTOR = 'director', 'Director'

    film_work = models.ForeignKey(FilmWork, on_delete=models.CASCADE, related_name='person_roles')
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    role = models.CharField(max_length=8, choices=RoleChoices.choices)

    class Meta:
        db_table = "content\".\"person_film_work"
        verbose_name = 'Персона фильма'
        verbose_name_plural = 'Персоны фильма'


class GenreFilmWork(TimeStampedMixin, UUIDMixin):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    film_work = models.ForeignKey(FilmWork, on_delete=models.CASCADE)

    class Meta:
        db_table = "content\".\"genre_film_work"
        verbose_name = 'Жанр фильма'
        verbose_name_plural = 'Жанры фильма'
