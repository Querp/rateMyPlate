# Generated by Django 5.0.8 on 2024-10-28 02:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0005_rename_malsheid_rating_taste_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerCompetition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, max_length=100, null=True)),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competition.competition')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competition.player')),
            ],
            options={
                'unique_together': {('player', 'competition')},
            },
        ),
    ]