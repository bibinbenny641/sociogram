# Generated by Django 4.1.4 on 2022-12-29 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminSide', '0004_user_active_user_admin_user_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='active',
        ),
    ]
