# Generated by Django 3.1.8 on 2021-05-28 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_auto_20210527_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='hotel',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='home.bvn'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.sign'),
        ),
        migrations.CreateModel(
            name='Restaura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=22)),
                ('phone1', models.IntegerField(max_length=22)),
                ('types', models.CharField(max_length=22)),
                ('no_of_members', models.IntegerField()),
                ('time', models.DateTimeField()),
                ('hotel', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='home.bvn')),
            ],
        ),
    ]
