# Generated by Django 4.2.10 on 2024-03-29 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='pic',
        ),
    ]
