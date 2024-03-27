# Generated by Django 4.2.11 on 2024-03-27 10:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FilmWork',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('creation_date', models.DateField(blank=True, null=True, verbose_name='Creation date')),
                ('rating', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Rating')),
                ('type', models.CharField(choices=[('movie', 'Movie'), ('tv_show', 'TV Show')], max_length=8, verbose_name='Type')),
                ('certificate', models.CharField(blank=True, max_length=512, null=True, verbose_name='Certificate')),
                ('file_path', models.FileField(blank=True, null=True, upload_to='movies/', verbose_name='File')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
                'db_table': 'content"."film_work',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
                'db_table': 'content"."genre',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('full_name', models.TextField(verbose_name='Full name')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Persons',
                'db_table': 'content"."person',
            },
        ),
        migrations.CreateModel(
            name='PersonFilmWork',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('role', models.CharField(choices=[('actor', 'Actor'), ('producer', 'Producer'), ('director', 'Director')], max_length=8, verbose_name='Role')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('film_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_roles', to='movies.filmwork', verbose_name='Film work')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='film_works', to='movies.person', verbose_name='Person')),
            ],
            options={
                'verbose_name': 'Персона фильма',
                'verbose_name_plural': 'Персоны фильма',
                'db_table': 'content"."person_film_work',
            },
        ),
        migrations.CreateModel(
            name='GenreFilmWork',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('film_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.filmwork', verbose_name='Film work')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.genre', verbose_name='Genre')),
            ],
            options={
                'verbose_name': 'Жанр фильма',
                'verbose_name_plural': 'Жанры фильма',
                'db_table': 'content"."genre_film_work',
            },
        ),
        migrations.AddField(
            model_name='filmwork',
            name='genres',
            field=models.ManyToManyField(related_name='film_works', through='movies.GenreFilmWork', to='movies.genre'),
        ),
    ]
