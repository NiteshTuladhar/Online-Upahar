# Generated by Django 3.1.2 on 2020-10-11 09:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Profile', '0005_auto_20201009_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('profile_image', models.ImageField(blank=True, default='images/img1.jpg', null=True, upload_to='user_profile_img')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'male'), ('Female', 'female'), ('Other', 'other')], max_length=30, null=True)),
                ('shop_name', models.CharField(blank=True, max_length=30, null=True)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]