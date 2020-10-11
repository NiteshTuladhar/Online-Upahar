# Generated by Django 3.1.2 on 2020-10-11 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SellerAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('account_name', models.CharField(max_length=50, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('token', models.CharField(blank=True, max_length=20, null=True)),
                ('shop_name', models.CharField(blank=True, max_length=50, null=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('send_first_email', models.BooleanField(default=False)),
                ('profile_create', models.BooleanField(default=False)),
                ('is_seller', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
