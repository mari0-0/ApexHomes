# Generated by Django 4.2.6 on 2023-11-05 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_alter_hotelroom_has_tv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='lot_size',
        ),
    ]
