# Generated by Django 4.1.3 on 2022-11-30 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminSide', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='staff',
        ),
    ]
