# Generated by Django 4.1 on 2022-08-29 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0007_order_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]