# Generated by Django 2.2.16 on 2020-11-05 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egystoreapp', '0007_auto_20201023_0144'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='location',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
