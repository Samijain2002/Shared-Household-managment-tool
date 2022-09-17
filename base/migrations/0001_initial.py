# Generated by Django 4.1.1 on 2022-09-10 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payday', models.DateField()),
                ('amount', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['payday'],
            },
        ),
        migrations.CreateModel(
            name='Tiffin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sami', models.IntegerField()),
                ('utsi', models.IntegerField()),
                ('vanshi', models.IntegerField()),
                ('meetu', models.IntegerField()),
                ('todays_data', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Water',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todays', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
