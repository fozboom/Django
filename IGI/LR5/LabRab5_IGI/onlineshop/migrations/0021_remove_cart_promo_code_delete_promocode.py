# Generated by Django 5.0.2 on 2024-05-18 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0020_promocode_cart_promo_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='promo_code',
        ),
        migrations.DeleteModel(
            name='PromoCode',
        ),
    ]
