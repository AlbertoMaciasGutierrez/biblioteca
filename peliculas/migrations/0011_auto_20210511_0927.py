# Generated by Django 3.1.7 on 2021-05-11 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0010_auto_20210510_1102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='peliculas',
        ),
        migrations.AddField(
            model_name='pelicula',
            name='actores',
            field=models.ManyToManyField(blank=True, related_name='actores', to='peliculas.Actor'),
        ),
    ]
