# Generated by Django 3.1.2 on 2020-10-11 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0009_account_is_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='is_seller',
        ),
    ]
