# Generated by Django 3.1.8 on 2021-05-25 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_city_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='des',
        ),
    ]
