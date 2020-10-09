# Generated by Django 3.1.2 on 2020-10-08 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0004_account_send_first_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('mobile', models.CharField(max_length=15)),
                ('profile_image', models.ImageField(blank=True, default='img/default_profile_img.jpg', null=True, upload_to='user_profile_img')),
                ('gender', models.CharField(choices=[('Male', 'male'), ('Female', 'female'), ('Other', 'other')], max_length=30)),
                ('location', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='account',
            name='address',
        ),
        migrations.RemoveField(
            model_name='account',
            name='contact_no',
        ),
        migrations.RemoveField(
            model_name='account',
            name='country',
        ),
        migrations.RemoveField(
            model_name='account',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='account',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='account',
            name='image',
        ),
    ]
