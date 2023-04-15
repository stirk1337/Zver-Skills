# Generated by Django 4.2 on 2023-04-15 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0004_skill_skill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='test',
        ),
        migrations.AddField(
            model_name='vacancy',
            name='company',
            field=models.CharField(default='ЗВЕР', max_length=250),
        ),
        migrations.CreateModel(
            name='SkillResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=100)),
                ('points', models.IntegerField(max_length=100)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancy.survey')),
            ],
        ),
    ]