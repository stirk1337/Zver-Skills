# Generated by Django 4.2 on 2023-04-16 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_useraccount_mentor_spec'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='is_read',
        ),
        migrations.AddField(
            model_name='notification',
            name='message',
            field=models.CharField(default='', max_length=300),
        ),
    ]
