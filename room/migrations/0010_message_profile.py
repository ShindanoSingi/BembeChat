# Generated by Django 3.2.14 on 2022-07-10 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0009_auto_20220710_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='room.profile'),
        ),
    ]
