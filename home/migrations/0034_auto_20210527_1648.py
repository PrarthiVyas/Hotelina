# Generated by Django 3.1.8 on 2021-05-28 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_auto_20210527_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0)),
                ('category', models.CharField(choices=[('YAY', 'AC'), ('NAC', 'NON-AC'), ('DEL', 'DELUX')], default='', max_length=3)),
                ('beds', models.IntegerField(default=0)),
                ('capacity', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.rooms'),
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]