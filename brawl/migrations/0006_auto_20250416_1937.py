# Generated by Django 2.2.28 on 2025-04-16 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brawl', '0005_deck_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='loses',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='deck',
            name='wins',
            field=models.IntegerField(default=0),
        ),
    ]
