# Generated by Django 3.2 on 2023-06-26 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='edms_id',
            field=models.IntegerField(default=123),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='entry_datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]