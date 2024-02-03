from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Loan
from .serializers import LoanEligibilitySerializer,CreateLoanSerializer,CustomerSerializer,ViewLoansSerializer,LoanSerializer
from customerapp.models import Customer
from .loan_calculator import LoanCalculator 
from datetime import datetime
 # Assuming you have a loan_calculator module

@api_view(['POST'])
def check_eligibility_view(request):
    # Validate and deserialize the input data
    serializer = LoanEligibilitySerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    # Extract data from the validated data
    customer_id = serializer.validated_data['customer_id']
    loan_amount = serializer.validated_data['loan_amount']
    interest_rate = serializer.validated_data['interest_rate']
    tenure = serializer.validated_data['tenure']

    # Dummy monthly salary for demonstration purposes
    monthly_salary = LoanCalculator.get_monthly_salary(customer_id)

    # Check loan eligibility
    approval, corrected_interest_rate, tenure, monthly_installment = LoanCalculator.check_loan_eligibility(
        customer_id, loan_amount, interest_rate, tenure, monthly_salary
    )

    # Prepare response data
    response_data = {
        'customer_id': customer_id,
        'approval': approval,
        'interest_rate': interest_rate,
        'corrected_interest_rate': corrected_interest_rate,
        'tenure': tenure,
        'monthly_installment': monthly_installment,
    }

    return Response(response_data)
@api_view(['POST'])
def create_loan_view(request):
    serializer = CreateLoanSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    customer_id = serializer.validated_data['customer_id']
    loan_amount = serializer.validated_data['loan_amount']
    interest_rate = serializer.validated_data['interest_rate']
    tenure = serializer.validated_data['tenure']

    monthly_salary = LoanCalculator.get_monthly_salary(customer_id)

    approval, corrected_interest_rate, tenure, monthly_installment = LoanCalculator.check_loan_eligibility(
        customer_id, loan_amount, interest_rate, tenure, monthly_salary
    )

    if not approval:
        response_data = {
            'loan_id': None,
            'customer_id': customer_id,
            'loan_approved': False,
            'message': 'Loan not approved based on eligibility criteria.',
            'monthly_installment': 0.0,
        }
    else:
        # Process the loan approval and create a Loan instance
        loan = Loan.objects.create(
            customer_id=customer_id,
            loan_amount=loan_amount,
            interest_rate=corrected_interest_rate,
            tenure=tenure,
            monthly_repayment=monthly_installment,
            emis_paid_on_time=0,
            start_date=datetime.now(),
            end_date=datetime.now(),  # You need to set the actual end date based on the tenure
        )

        response_data = {
            'loan_id': loan.id,
            'customer_id': customer_id,
            'loan_approved': True,
            'message': 'Loan approved and processed successfully.',
            'monthly_installment': float(monthly_installment),
        }

    return Response(response_data)
@api_view(['GET'])
def view_loan_details(request, loan_id):
    # Retrieve loan details
    loan = get_object_or_404(Loan, loan_id=loan_id)

    # Serialize loan data
    serializer = LoanSerializer(loan)

    # Prepare customer details
    customer_details = {
        'id': loan.customer_id.customer_id,
        'first_name': loan.customer_id.first_name,
        'last_name': loan.customer_id.last_name,
        'phone_number': loan.customer_id.phone_number,
        'age': loan.customer_id.age,
    }

    # Construct the response body
    response_data = {
        'loan_id': loan.loan_id,
        'customer': customer_details,
        'loan_amount': loan.loan_amount,
        'interest_rate': loan.interest_rate,
        'monthly_installment': loan.monthly_repayment,
        'tenure': loan.tenure,
    }

    return Response(response_data)

@api_view(['GET'])
def view_loans_by_customer(request, customer_id):
    loans = Loan.objects.filter(customer_id=customer_id)

    loan_items = []
    for loan in loans:
        repayments_left = loan.tenure - loan.emis_paid_on_time
        loan_items.append({
            'loan_id': loan.id,
            'loan_amount': float(loan.loan_amount),
            'interest_rate': float(loan.interest_rate),
            'monthly_installment': float(loan.monthly_repayment),
            'repayments_left': repayments_left,
        })

    response_data = {
        'loans': loan_items,
    }

    serializer = ViewLoansSerializer(data=response_data)
    serializer.is_valid()

    return Response(serializer.validated_data)  