# Generated by Django 3.1.7 on 2021-05-10 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0009_auto_20210507_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='peliculas',
            field=models.ManyToManyField(blank=True, related_name='peliculas', to='peliculas.Pelicula'),
        ),
    ]