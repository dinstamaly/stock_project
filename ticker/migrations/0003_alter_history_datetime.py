# Generated by Django 3.2.2 on 2021-05-09 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0002_alter_history_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='datetime',
            field=models.DateTimeField(),
        ),
    ]
