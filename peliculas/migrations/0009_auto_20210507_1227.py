# Generated by Django 3.1.7 on 2021-05-07 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0008_auto_20210507_1114'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pelicula',
            options={'ordering': ['-fecha_publicacion'], 'verbose_name': 'pelicula', 'verbose_name_plural': 'peliculas'},
        ),
        migrations.AlterField(
            model_name='actor',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='actores', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='peliculas',
            field=models.ManyToManyField(related_name='peliculas', to='peliculas.Pelicula'),
        ),
        migrations.AlterField(
            model_name='director',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='directores', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='peliculas', verbose_name='Imagen'),
        ),
    ]
