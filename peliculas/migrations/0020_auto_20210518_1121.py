# Generated by Django 3.1.7 on 2021-05-18 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0019_auto_20210513_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioVoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'usuarioVoto',
                'verbose_name_plural': 'usuariosVotos',
                'ordering': ['nombre'],
            },
        ),
        migrations.AddField(
            model_name='pelicula',
            name='voto_usuarios',
            field=models.ManyToManyField(blank=True, related_name='voto_usuarios', to='peliculas.UsuarioVoto'),
        ),
    ]
