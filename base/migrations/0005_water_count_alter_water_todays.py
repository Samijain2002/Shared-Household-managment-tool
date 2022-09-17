# Generated by Django 4.1.1 on 2022-09-10 11:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_tiffin_shift_tiffin_today_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='water',
            name='count',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='water',
            name='todays',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
