# Generated by Django 3.1.8 on 2021-05-26 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20210525_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='bvn',
            name='entry',
            field=models.CharField(default='', max_length=22),
        ),
    ]
