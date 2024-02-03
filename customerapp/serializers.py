# serializers.py
# serializers.py

from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    # Your serializer fields...

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'age', 'monthly_income', 'phone_number']
    

    def create(self, validated_data):
        # Calculate the approved_limit based on monthly_income
        monthly_income = validated_data['monthly_income']
        validated_data['approved_limit'] = round(36 * monthly_income, -5)  # Round to the nearest lakh

        # Create and return the instance
        return super().create(validated_data)

