from django.db import models
from customerapp.models import Customer

class Loan(models.Model):
    #id = models.AutoField(primary_key=True)
    #customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    customer_id=models.ForeignKey(Customer, on_delete=models.CASCADE)

    loan_id = models.IntegerField()
    loan_amount = models.FloatField()
    tenure = models.FloatField()
    interest_rate = models.FloatField()
    monthly_repayment = models.FloatField()
    emis_paid_on_time = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    

