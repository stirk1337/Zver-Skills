# Generated by Django 4.2 on 2023-04-15 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0009_remove_test_difficulty_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='false1',
            new_name='opt1',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='false2',
            new_name='opt2',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='false3',
            new_name='opt3',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='true1',
            new_name='opt4',
        ),
    ]