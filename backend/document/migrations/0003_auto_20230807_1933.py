# Generated by Django 3.2 on 2023-08-07 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0002_auto_20230626_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='datetime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='document',
            name='entry_datetime',
            field=models.DateTimeField(),
        ),
    ]
