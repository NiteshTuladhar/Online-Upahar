# Generated by Django 3.1.2 on 2020-10-09 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0003_auto_20201009_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Male', 'male'), ('Female', 'female'), ('Other', 'other')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
    ]