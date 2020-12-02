# Generated by Django 3.1.2 on 2020-12-01 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0026_auto_20201129_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingadress',
            name='city',
        ),
        migrations.RemoveField(
            model_name='shippingadress',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='shippingadress',
            name='zone',
        ),
        migrations.AddField(
            model_name='shippingadress',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='email address'),
        ),
        migrations.AddField(
            model_name='shippingadress',
            name='first_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='shippingadress',
            name='last_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]