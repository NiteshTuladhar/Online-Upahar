# Generated by Django 3.1.2 on 2020-11-22 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0020_order_order_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_items',
            field=models.ManyToManyField(to='Products.OrderItem'),
        ),
    ]