# Generated by Django 3.1.8 on 2021-05-15 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210514_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sign',
            name='pass1',
            field=models.CharField(blank=True, max_length=122, null=True),
        ),
    ]
