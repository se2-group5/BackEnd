# Generated by Django 4.0.4 on 2022-04-29 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='puntaje',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
    ]
