# Generated by Django 3.2.5 on 2021-07-22 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tracks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_id', models.IntegerField(default=0)),
                ('artist_id', models.IntegerField(default=0)),
                ('year', models.IntegerField(default=0)),
                ('popularity', models.IntegerField(default=0)),
                ('release_date', models.IntegerField(default=0)),
                ('acousticness', models.FloatField(default=0)),
                ('danceability', models.FloatField(default=0)),
                ('duration_ms', models.FloatField(default=0)),
                ('energy', models.FloatField(default=0)),
                ('instrumentalness', models.FloatField(default=0)),
                ('liveness', models.FloatField(default=0)),
                ('loudness', models.FloatField(default=0)),
                ('valence', models.FloatField(default=0)),
                ('speechiness', models.FloatField(default=0)),
                ('tempo', models.FloatField(default=0)),
                ('key', models.IntegerField(default=0)),
                ('mode', models.IntegerField(default=0)),
            ],
        ),
    ]
