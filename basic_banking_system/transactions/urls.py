
from django.urls import path
from . import views

app_name = 'transactions'

urlpatterns = [
    
    path('',views.home,name = 'home'),
    path('customers',views.customer,name = 'customer'),
    path('transfer',views.transfer,name = 'transfer'),
    path('transop',views.transop,name = 'transop'),
    path('transaction_table',views.transaction_table, name = 'transaction_table'),
]