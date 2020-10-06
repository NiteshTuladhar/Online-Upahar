

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),

                ('account_name', models.CharField(max_length=50, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, default='user/unknown.jpg', null=True, upload_to='user/')),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'male'), ('Female', 'female'), ('Other', 'other')], max_length=30, null=True)),
                ('contact_no', models.CharField(blank=True, max_length=15, null=True)),

                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('token', models.CharField(blank=True, max_length=20, null=True)),
                ('is_verified', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
