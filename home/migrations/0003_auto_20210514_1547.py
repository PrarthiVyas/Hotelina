# Generated by Django 3.1.8 on 2021-05-15 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_sign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sign',
            name='email',
            field=models.EmailField(blank=True, max_length=122, null=True),
        ),
    ]
