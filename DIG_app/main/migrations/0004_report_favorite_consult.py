# Generated by Django 4.0.4 on 2022-05-13 17:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_user_rating_alter_user_telephone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('occupation_status', models.CharField(max_length=20)),
                ('internet_status', models.DecimalField(decimal_places=1, max_digits=2)),
                ('rating_business', models.DecimalField(decimal_places=1, max_digits=2)),
                ('report_support', models.IntegerField()),
                ('comments', models.TextField()),
                ('business_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.business', verbose_name='UserID')),
                ('user_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, verbose_name='UserID')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.business', verbose_name='UserID')),
                ('user_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, verbose_name='UserID')),
            ],
        ),
        migrations.CreateModel(
            name='Consult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('business_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.business', verbose_name='UserID')),
                ('user_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, verbose_name='UserID')),
            ],
        ),
    ]
