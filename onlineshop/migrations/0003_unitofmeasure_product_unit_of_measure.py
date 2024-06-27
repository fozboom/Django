# Generated by Django 5.0.2 on 2024-05-01 21:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0002_manufacturer_product_manufacturer'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnitOfMeasure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='unit_of_measure',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='onlineshop.unitofmeasure'),
        ),
    ]