# Generated by Django 4.0.4 on 2022-05-01 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_establecimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='establecimiento',
            name='capacidad',
            field=models.IntegerField(),
        ),
    ]