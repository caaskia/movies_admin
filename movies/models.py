from django.utils.translation import gettext_lazy as _

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

    title = models.CharField(_('Title'), max_length=255)
    description = models.TextField(_('Description'), blank=True, null=True)
    creation_date = models.DateField(_('Creation date'), blank=True, null=True)
    rating = models.FloatField(_('Rating'), blank=True,
                               validators=[MinValueValidator(0),
                                           MaxValueValidator(100)])
    type = models.CharField(_('Type'), max_length=8, choices=TypeChoices.choices)
    genres = models.ManyToManyField('Genre', through='GenreFilmWork', related_name='film_works')
    certificate = models.CharField(_('Certificate'), max_length=512, blank=True)
    # Параметр upload_to указывает, в какой подпапке будут храниться загружемые файлы.
    # Базовая папка указана в файле настроек как MEDIA_ROOT
    file_path = models.FileField(_('File'), blank=True, null=True, upload_to='movies/')

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


class GenreFilmWork(UUIDMixin):
    film_work = models.ForeignKey(FilmWork, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"genre_film_work"
        verbose_name = 'Жанр фильма'
        verbose_name_plural = 'Жанры фильма'


class Person(TimeStampedMixin, UUIDMixin):
    full_name = models.TextField()

    class Meta:
        db_table = "content\".\"person"
        verbose_name = 'Персона'
        verbose_name_plural = 'Персоны'

    def __str__(self):
        return self.full_name


class PersonFilmWork(UUIDMixin):
    class RoleChoices(models.TextChoices):
        ACTOR = 'actor', 'Actor'
        PRODUCER = 'producer', 'Producer'
        DIRECTOR = 'director', 'Director'

    film_work = models.ForeignKey(FilmWork, on_delete=models.CASCADE, related_name='person_roles')
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    role = models.CharField(max_length=8, choices=RoleChoices.choices)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"person_film_work"
        verbose_name = 'Персона фильма'
        verbose_name_plural = 'Персоны фильма'