# Generated by Django 3.1.6 on 2023-06-23 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_index', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='PurpleSensors',
        ),
    ]
