# Generated by Django 3.2.14 on 2022-07-10 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0023_message_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='message_color',
            field=models.CharField(default='lightblue', max_length=255),
        ),
    ]
