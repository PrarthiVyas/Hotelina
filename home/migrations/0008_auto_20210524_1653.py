# Generated by Django 3.1.8 on 2021-05-25 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_city_des'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
