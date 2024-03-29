# Generated by Django 3.1.2 on 2020-12-07 09:55

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0029_merge_20201206_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_category', models.CharField(max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='main_category', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category', models.CharField(max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='sub_category', unique=True)),
            ],
        ),
    ]
