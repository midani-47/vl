# Generated by Django 5.0.6 on 2024-05-31 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_followers_alter_profile_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='followers',
        ),
    ]
