# Generated by Django 4.2 on 2023-04-15 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='false1',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
    ]