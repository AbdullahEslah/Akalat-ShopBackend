# Generated by Django 2.2 on 2021-06-20 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('egystoreapp', '0008_driver_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='image',
            field=models.ImageField(blank=True, upload_to='meal_images/'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant', to='egystoreapp.Restaurant'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='egystoreapp.Customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='egystoreapp.Driver'),
        ),
        migrations.AlterField(
            model_name='order',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='egystoreapp.Restaurant'),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='meal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='egystoreapp.Meal'),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_details', to='egystoreapp.Order'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='logo',
            field=models.ImageField(blank=True, upload_to='restaurant_logos/'),
        ),
    ]
