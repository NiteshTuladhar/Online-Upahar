# Generated by Django 3.1.2 on 2020-10-09 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0006_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='profile_create',
            field=models.BooleanField(default=True),
        ),
    ]
