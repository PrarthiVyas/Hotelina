# Generated by Django 3.1.8 on 2021-05-26 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_remove_bvn_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='bvn',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='bvn',
            name='phone',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
