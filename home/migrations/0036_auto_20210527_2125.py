# Generated by Django 3.1.8 on 2021-05-28 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_auto_20210527_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='category',
            field=models.CharField(choices=[('DELUX', 'DELUX'), ('AC', 'AC'), ('NON-AC', 'NON-AC')], default='AC', max_length=3),
        ),
    ]
