# Generated by Django 3.1.8 on 2021-05-26 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_remove_bvn_ph'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bvn',
            name='email',
        ),
    ]
