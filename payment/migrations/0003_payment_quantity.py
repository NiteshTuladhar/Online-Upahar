# Generated by Django 3.1.2 on 2020-11-29 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_auto_20201129_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='quantity',
            field=models.IntegerField(max_length=10, null=True),
        ),
    ]