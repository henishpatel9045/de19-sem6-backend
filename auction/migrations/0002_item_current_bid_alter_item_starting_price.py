# Generated by Django 4.1.7 on 2023-03-29 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='current_bid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='item',
            name='starting_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
