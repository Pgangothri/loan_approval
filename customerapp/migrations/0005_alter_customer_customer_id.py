# Generated by Django 5.0.1 on 2024-02-03 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0004_alter_customer_customer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.AutoField(default=301, primary_key=True, serialize=False),
        ),
    ]