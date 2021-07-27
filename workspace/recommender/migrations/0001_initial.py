# Generated by Django 3.2.5 on 2021-07-26 05:58

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
                ('valence', models.FloatField(default=0)),
                ('year', models.IntegerField(default=0)),
                ('acousticness', models.FloatField(default=0)),
                ('artists', models.CharField(default='', max_length=200)),
                ('danceability', models.FloatField(default=0)),
                ('duration_ms', models.FloatField(default=0)),
                ('energy', models.FloatField(default=0)),
                ('explicit', models.IntegerField(default=0)),
                ('track_id', models.CharField(default='', max_length=200)),
                ('instrumentalness', models.FloatField(default=0)),
                ('key', models.IntegerField(default=0)),
                ('liveness', models.FloatField(default=0)),
                ('loudness', models.FloatField(default=0)),
                ('mode', models.IntegerField(default=0)),
                ('track_name', models.CharField(default='', max_length=200)),
                ('popularity', models.IntegerField(default=0)),
                ('release_date', models.IntegerField(default=0)),
                ('speechiness', models.FloatField(default=0)),
                ('tempo', models.FloatField(default=0)),
            ],
        ),
    ]
