# Generated by Django 3.1.2 on 2020-10-08 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0003_account_account_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='send_first_email',
            field=models.BooleanField(default=False),
        ),
    ]
