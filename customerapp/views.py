# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Customer
from .serializers import CustomerSerializer

@api_view(['POST'])
def register_customer(request):
    serializer = CustomerSerializer(data=request.data)
    
    if serializer.is_valid():
        # Calculate approved_limit based on the provided monthly_income
        monthly_income = serializer.validated_data['monthly_income']
        approved_limit = round(36 * monthly_income, -5)  # Rounded to the nearest lakh

        # Save to the database
        customer = serializer.save(approved_limit=approved_limit)

        # Prepare response data
        response_data = {
            'customer_id': customer.customer_id,
            'name': f"{customer.first_name} {customer.last_name}",
            'age': customer.age,
            'monthly_income': customer.monthly_income,
            'approved_limit': customer.approved_limit,
            'phone_number': customer.phone_number,
        }

        return Response(response_data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
