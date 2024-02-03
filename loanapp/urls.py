from django.urls import path
from . import views
urlpatterns=[
    path('check-eligibility/',views.check_eligibility_view,name='check_eligibility_view'),
     path('create-loan/', views.create_loan_view, name='create_loan'),
     path('view-loan/<int:loan_id>/', views.view_loan_details, name='view_loan_details'),
      path('view-loans/<int:customer_id>/', views.view_loans_by_customer, name='view_loans_by_customer'),

     
]