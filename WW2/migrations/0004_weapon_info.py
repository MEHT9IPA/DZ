# Generated by Django 3.1.5 on 2021-01-19 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WW2', '0003_weapon'),
    ]

    operations = [
        migrations.AddField(
            model_name='weapon',
            name='info',
            field=models.TextField(default='-', verbose_name='Краткая информация'),
        ),
    ]
