# Generated by Django 2.2.5 on 2019-12-22 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_auto_20191222_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='address',
            field=models.CharField(max_length=150),
        ),
    ]