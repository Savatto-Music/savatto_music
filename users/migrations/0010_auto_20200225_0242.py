# Generated by Django 3.0.3 on 2020-02-25 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20200225_0238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='urlsong1',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='urlsong2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='urlsong3',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
