# Generated by Django 4.2.6 on 2023-11-08 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0016_listing_contact_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='contact_info',
            field=models.PositiveBigIntegerField(),
        ),
    ]