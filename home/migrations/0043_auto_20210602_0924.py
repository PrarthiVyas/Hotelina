# Generated by Django 3.1.8 on 2021-06-02 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0042_auto_20210602_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='category',
            field=models.CharField(choices=[('DELUX', 'DELUX'), ('AC', 'AC'), ('NON-AC', 'NON-AC')], default='AC', max_length=10),
        ),
    ]