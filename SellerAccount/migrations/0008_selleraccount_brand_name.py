# Generated by Django 3.1.2 on 2021-02-06 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SellerAccount', '0007_auto_20201215_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='selleraccount',
            name='brand_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
