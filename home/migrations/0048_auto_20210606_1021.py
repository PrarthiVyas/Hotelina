# Generated by Django 3.1.8 on 2021-06-06 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0047_auto_20210604_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='category',
            field=models.CharField(choices=[('DELUX', 'DELUX'), ('NON-AC', 'NON-AC'), ('AC', 'AC')], default='AC', max_length=10),
        ),
    ]
