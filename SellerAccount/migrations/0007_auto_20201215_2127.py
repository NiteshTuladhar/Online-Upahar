# Generated by Django 3.1.2 on 2020-12-15 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SellerAccount', '0006_auto_20201215_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_seller_account',
            name='business_type',
            field=models.CharField(blank=True, choices=[('Sole Proprietorship', 'Sole Proprietorship'), ('Partnership', 'Partnership'), ('Corporation', 'Corporation'), ('Shop', 'Shop')], max_length=30, null=True),
        ),
    ]
