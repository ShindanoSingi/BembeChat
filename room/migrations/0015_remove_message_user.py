# Generated by Django 3.2.14 on 2022-07-10 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0014_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
    ]
