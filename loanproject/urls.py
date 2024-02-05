
from django.contrib import admin
from django.urls import path ,include
from customerapp import views
from loanapp import urls as loanapp_urls

#from loanapp import views


urlpatterns = [
    
   path('register/',views.register_customer, name='register_customer'),
  path('',include(loanapp_urls)),
]
