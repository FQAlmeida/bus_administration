# Generated by Django 2.1.7 on 2019-03-23 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus_control', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passager',
            name='document',
            field=models.CharField(max_length=11),
        ),
    ]
