# Generated by Django 3.1.8 on 2021-05-28 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_auto_20210527_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.CharField(choices=[('NAC', 'NON-AC'), ('YAY', 'AC'), ('DEL', 'DELUX')], default='', max_length=3),
        ),
        migrations.CreateModel(
            name='booking',
            fields=[
               
                ('check_in', models.DateTimeField()),
                ('check_out', models.DateTimeField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.bvn')),
            ],
        ),
    ]
