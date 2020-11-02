# Generated by Django 3.1.2 on 2020-10-28 12:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Products', '0015_auto_20201028_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='liked',
            field=models.ManyToManyField(blank=True, default=None, related_name='liked', to=settings.AUTH_USER_MODEL),
        ),
    ]
