# Generated by Django 3.1.7 on 2021-05-19 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0023_auto_20210519_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valoracion', models.DecimalField(choices=[(0.0, 0), (1.0, 1), (2.0, 2), (3.0, 3), (4.0, 4), (5.0, 5), (6.0, 6), (7.0, 7), (8.0, 8), (9.0, 9), (10.0, 10)], decimal_places=1, default=0.0, max_digits=3)),
                ('usuario', models.CharField(max_length=40)),
            ],
        ),
        migrations.RemoveField(
            model_name='pelicula',
            name='valoracionTotal',
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='actores',
            field=models.ManyToManyField(blank=True, related_name='actores', to='peliculas.Actor'),
        ),
        migrations.RemoveField(
            model_name='pelicula',
            name='valoracion',
        ),
        migrations.AddField(
            model_name='pelicula',
            name='valoracion',
            field=models.ManyToManyField(blank=True, related_name='actores', to='peliculas.Voto'),
        ),
    ]
