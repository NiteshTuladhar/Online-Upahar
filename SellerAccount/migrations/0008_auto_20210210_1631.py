# Generated by Django 3.1.2 on 2021-02-10 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SellerAccount', '0007_auto_20201215_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_seller_account',
            name='brand_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='selleraccount',
            name='brand_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
