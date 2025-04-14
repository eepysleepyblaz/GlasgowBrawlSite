# Generated by Django 2.2.28 on 2025-04-14 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('event_date', models.DateTimeField()),
                ('player', models.CharField(max_length=101)),
                ('deck_list', models.CharField(max_length=99999)),
            ],
        ),
    ]
