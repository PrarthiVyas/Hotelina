# Generated by Django 3.1.8 on 2021-05-28 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_auto_20210527_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaura',
            name='time',
            field=models.CharField(max_length=22),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='category',
            field=models.CharField(choices=[('DELUX', 'DELUX'), ('AC', 'AC'), ('NON-AC', 'NON-AC')], default='AC', max_length=3),
        ),
    ]
