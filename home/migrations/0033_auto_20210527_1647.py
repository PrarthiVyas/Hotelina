# Generated by Django 3.1.8 on 2021-05-28 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_auto_20210527_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.CharField(choices=[('DEL', 'DELUX'), ('NAC', 'NON-AC'), ('YAY', 'AC')], default='', max_length=3),
        ),
    ]
