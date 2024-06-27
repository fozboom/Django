# Generated by Django 5.0.2 on 2024-05-19 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0026_order_pickup_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(default='default@email.com', max_length=254),
        ),
        migrations.AddField(
            model_name='employee',
            name='job_description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='employee',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='employee_photos/'),
        ),
    ]