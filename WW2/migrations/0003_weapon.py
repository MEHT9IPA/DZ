# Generated by Django 3.1.5 on 2021-01-19 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WW2', '0002_auto_20210118_2026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Техника')),
                ('users', models.ManyToManyField(to='WW2.Country')),
            ],
        ),
    ]
