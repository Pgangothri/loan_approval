# Generated by Django 5.0.1 on 2024-02-03 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0006_alter_customer_customer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.AutoField(default=303, primary_key=True, serialize=False),
        ),
    ]
