# Generated by Django 3.1.2 on 2020-10-11 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0010_remove_account_is_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_seller',
            field=models.BooleanField(default=False),
        ),
    ]
