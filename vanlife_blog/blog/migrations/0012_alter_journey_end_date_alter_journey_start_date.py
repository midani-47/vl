# Generated by Django 5.0.6 on 2024-05-31 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_journey_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='end_date',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='journey',
            name='start_date',
            field=models.CharField(max_length=100),
        ),
    ]