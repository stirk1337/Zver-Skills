# Generated by Django 4.2 on 2023-04-15 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0010_rename_false1_question_opt1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='right',
            field=models.CharField(default='', max_length=100),
        ),
    ]