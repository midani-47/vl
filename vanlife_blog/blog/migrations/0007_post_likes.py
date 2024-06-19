# Generated by Django 5.0.6 on 2024-05-31 09:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_delete_blog'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
