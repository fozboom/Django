# Generated by Django 5.0.2 on 2024-05-18 17:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0017_alter_order_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlineshop.client')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlineshop.product')),
            ],
        ),
    ]
