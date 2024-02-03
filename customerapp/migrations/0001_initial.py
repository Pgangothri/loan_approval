# Generated by Django 5.0.1 on 2024-01-31 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('phone_number', models.BigIntegerField()),
                ('monthly_income', models.DecimalField(decimal_places=2, max_digits=20)),
                ('approved_limit', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]