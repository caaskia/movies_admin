# Generated by Django 4.2.11 on 2024-04-07 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0004_alter_personfilmwork_film_work"),
    ]

    operations = [
        migrations.AlterField(
            model_name="personfilmwork",
            name="person",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="personfilmwork",
                to="movies.person",
                verbose_name="Person",
            ),
        ),
    ]
