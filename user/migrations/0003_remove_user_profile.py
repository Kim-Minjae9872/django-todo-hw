# Generated by Django 4.2.4 on 2023-09-04 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile',
        ),
    ]
