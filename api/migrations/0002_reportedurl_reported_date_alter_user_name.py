# Generated by Django 4.2.3 on 2023-07-18 07:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportedurl',
            name='reported_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 18, 7, 48, 39, 409703, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
    ]