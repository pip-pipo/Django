# Generated by Django 3.1.1 on 2020-10-24 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0002_auto_20201023_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=200),
        ),
    ]
