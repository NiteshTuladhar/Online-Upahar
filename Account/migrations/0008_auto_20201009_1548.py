# Generated by Django 3.1.2 on 2020-10-09 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0007_account_profile_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profile_create',
            field=models.BooleanField(default=False),
        ),
    ]