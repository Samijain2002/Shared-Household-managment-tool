# Generated by Django 4.1.1 on 2022-09-10 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiffin',
            name='meetu',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tiffin',
            name='sami',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tiffin',
            name='todays_data',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='tiffin',
            name='utsi',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tiffin',
            name='vanshi',
            field=models.IntegerField(default=0),
        ),
    ]
