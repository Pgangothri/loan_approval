# models.py
from django.db import models
class Customer(models.Model):
    customer_id=models.AutoField(primary_key=True, serialize=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    phone_number = models.BigIntegerField()
    monthly_income = models.DecimalField(max_digits=20, decimal_places=2)
    approved_limit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
