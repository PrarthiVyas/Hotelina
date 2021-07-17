# Generated by Django 3.1.8 on 2021-05-26 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_auto_20210525_2155'),
    ]

    operations = [
        migrations.CreateModel(
            name='baroda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('area', models.CharField(default='', max_length=120)),
                ('cat1', models.CharField(default='', max_length=22)),
                ('cat2', models.CharField(default='', max_length=22)),
                ('cat3', models.CharField(default='', max_length=22)),
                ('entry1', models.CharField(default='', max_length=22)),
                ('entry2', models.CharField(default='', max_length=22)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='bvn',
            name='oiw',
        ),
    ]
