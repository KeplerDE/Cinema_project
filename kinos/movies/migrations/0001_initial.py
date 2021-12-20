# Generated by Django 4.0 on 2021-12-20 05:55

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.PositiveSmallIntegerField(default=0, verbose_name='Alter')),
                ('description', models.TextField(verbose_name='Beschreibung')),
                ('image', models.ImageField(upload_to='actors/', verbose_name='Bildschirmbild')),
            ],
            options={
                'verbose_name': 'Akteuren und Regisseure',
                'verbose_name_plural': 'Akteuren und Regisseure',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Kategorie')),
                ('description', models.TextField(verbose_name='Beschreibung')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Kategorie',
                'verbose_name_plural': 'Kategorien',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Beschreibung')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Name')),
                ('tagline', models.CharField(default='', max_length=100, verbose_name='Slogan')),
                ('description', models.TextField(verbose_name='Beschreibung')),
                ('poster', models.ImageField(upload_to='movies/', verbose_name='Poster')),
                ('year', models.PositiveSmallIntegerField(default=2019, verbose_name='Veröffentlichungsdatum')),
                ('country', models.CharField(max_length=30, verbose_name='Land')),
                ('world_premiere', models.DateField(default=datetime.date.today, verbose_name='Premiere in der Welt')),
                ('budget', models.PositiveIntegerField(default=0, help_text='Die Summe im Euro zu bezeichnen', verbose_name='Budget')),
                ('fees_in_usa', models.PositiveSmallIntegerField(default=0, help_text='Die Summe im Euro zu bezeichnen', verbose_name='Gebühren in USA')),
                ('fees_in_world', models.PositiveIntegerField(default=0, help_text='Die Summe im Euro zu bezeichnen', verbose_name='Gebühren in Welt')),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='Konzept')),
                ('actors', models.ManyToManyField(related_name='film_actor', to='movies.Actor', verbose_name='Akteuren')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.category', verbose_name='Kategorie')),
                ('directors', models.ManyToManyField(related_name='film_director', to='movies.Actor', verbose_name='Regisseure')),
                ('genres', models.ManyToManyField(to='movies.Genre', verbose_name='Genres')),
            ],
            options={
                'verbose_name': 'Film',
                'verbose_name_plural': 'Filme',
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField(default=0, verbose_name='Bedeutung')),
            ],
            options={
                'verbose_name': 'Der Stern des Ratings',
                'verbose_name_plural': 'Die Sterne des Ratings',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('text', models.TextField(max_length=5000, verbose_name='Meldung')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie', verbose_name='Film')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.reviews', verbose_name='Haupt')),
            ],
            options={
                'verbose_name': 'Bewertung',
                'verbose_name_plural': 'Bewertungen',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP Adresse')),
                ('movie', models.ForeignKey(on_delete=django.db.models.fields.CharField, to='movies.movie', verbose_name='Film')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.ratingstar', verbose_name='Stern')),
            ],
            options={
                'verbose_name': 'Der Stern des Ratings',
                'verbose_name_plural': 'Die Sterne des Ratings',
            },
        ),
        migrations.CreateModel(
            name='MovieShots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titel')),
                ('description', models.TextField(verbose_name='Beschreibung')),
                ('image', models.ImageField(upload_to='movie_shots/', verbose_name='Bildschirmbild')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie', verbose_name='Film')),
            ],
            options={
                'verbose_name': 'Die Fachkraft aus dem Film',
                'verbose_name_plural': 'Die Fachkräfte aus dem Film',
            },
        ),
    ]
