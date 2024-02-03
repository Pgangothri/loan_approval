from datetime import datetime
from django.db import models
from .models import Loan
from customerapp.models import Customer
from decimal import Decimal

class LoanCalculator:
    @staticmethod
    def calculate_past_loans_paid_on_time(customer_id):
        total_loans = Loan.objects.filter(customer_id=customer_id).count()
        on_time_loans = Loan.objects.filter(customer_id=customer_id, emis_paid_on_time__gte=total_loans / 2).count()

        if total_loans > 0:
            return (on_time_loans / total_loans) * 100
        else:
            return 0

    @staticmethod
    def calculate_monthly_installment(loan_amount, interest_rate, tenure):
        loan_amount_decimal = Decimal(str(loan_amount))
        interest_rate_decimal = Decimal(str(interest_rate))

        monthly_interest_rate = (interest_rate_decimal / 100) / 12
        total_payments = Decimal(str(tenure))

        # Use Decimal types consistently in the calculation
        return float(loan_amount_decimal * (monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments) /
                     ((1 + monthly_interest_rate) ** total_payments - 1))

    @staticmethod
    def calculate_loan_activity_in_current_year(customer_id):
        current_year = datetime.now().year
        return Loan.objects.filter(customer_id=customer_id, start_date__year=current_year).count()

    @staticmethod
    def calculate_loan_approved_volume(customer_id):
        return Loan.objects.filter(customer_id=customer_id).count()

    @staticmethod
    def calculate_credit_score(customer_id):
        past_loans_paid_on_time = LoanCalculator.calculate_past_loans_paid_on_time(customer_id)
        loan_activity_in_current_year = LoanCalculator.calculate_loan_activity_in_current_year(customer_id)
        loan_approved_volume = LoanCalculator.calculate_loan_approved_volume(customer_id)

        if past_loans_paid_on_time == 0 or loan_activity_in_current_year == 0 or loan_approved_volume == 0:
            return 0

        return (past_loans_paid_on_time + loan_activity_in_current_year) / loan_approved_volume
        



    @staticmethod
    def check_loan_eligibility(customer_id, loan_amount, interest_rate, tenure, monthly_salary):
        credit_score = LoanCalculator.calculate_credit_score(customer_id)
        if credit_score > 50:
            approval = True
        elif 30 < credit_score <= 50 and interest_rate > 12:
            approval = True
        elif 10 < credit_score <= 30 and interest_rate > 16:
            approval = True
        elif credit_score <= 10:
            approval = False
        else:
            approval = False

        credit_limit = 20
        corrected_interest_rate = min(interest_rate, credit_limit)

        # Check if the sum of all current EMIs is greater than 50% of monthly salary
        total_current_emis = Loan.objects.filter(customer_id=customer_id, end_date__gte=datetime.now()).aggregate(total_current_emis=models.Sum('monthly_repayment'))['total_current_emis'] or 0

        if total_current_emis > 0.5 *float(LoanCalculator.get_monthly_salary(customer_id)):
            approval = False

        # Additional logic for calculating monthly installment, if needed
        monthly_installment = LoanCalculator.calculate_monthly_installment(loan_amount, interest_rate, tenure)

        return approval, corrected_interest_rate, tenure, monthly_installment
    @staticmethod
    def get_monthly_salary(customer_id):
        try:
            loans = Loan.objects.filter(customer_id=customer_id)
            if loans.exists():
                latest_loan = loans.order_by('-end_date').first()  # Order by end_date in descending order
                customer = latest_loan.customer_id
                return customer.monthly_income
            # Assuming you want to get the monthly_income from the latest loan record
            else:
                return 0
        except Loan.DoesNotExist:
            return 0


    
    
