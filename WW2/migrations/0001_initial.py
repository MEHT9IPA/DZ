# Generated by Django 3.1.5 on 2021-01-18 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alliance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Фракция')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Страна')),
                ('flag', models.ImageField(upload_to='flags')),
                ('info', models.TextField(verbose_name='Краткая информация')),
                ('population', models.FloatField(verbose_name='Население')),
                ('area', models.FloatField(verbose_name='Площадь')),
                ('ally_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WW2.alliance')),
            ],
        ),
    ]
