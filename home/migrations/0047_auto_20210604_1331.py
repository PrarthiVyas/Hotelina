# Generated by Django 3.1.8 on 2021-06-05 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0046_auto_20210604_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='category',
            field=models.CharField(choices=[('NON-AC', 'NON-AC'), ('DELUX', 'DELUX'), ('AC', 'AC')], default='AC', max_length=10),
        ),
    ]
