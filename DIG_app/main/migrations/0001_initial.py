# Generated by Django 4.0.4 on 2022-04-29 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('puntaje', models.DecimalField(decimal_places=1, max_digits=1)),
                ('correo', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
    ]
