# Generated by Django 3.0 on 2020-01-26 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200118_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to='users/pictures'),
        ),
    ]
