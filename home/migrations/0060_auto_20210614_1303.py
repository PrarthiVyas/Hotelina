# Generated by Django 3.1.8 on 2021-06-15 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0059_auto_20210614_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='day',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
