# Generated by Django 5.0.8 on 2024-10-28 11:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0007_remove_satay_id_alter_satay_cook'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='satay',
            name='competition',
        ),
        migrations.AlterField(
            model_name='rating',
            name='rater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competition.playercompetition'),
        ),
    ]
