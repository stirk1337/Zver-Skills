# Generated by Django 4.2 on 2023-04-15 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0006_vacancy_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='points',
            field=models.IntegerField(default=60),
        ),
    ]
