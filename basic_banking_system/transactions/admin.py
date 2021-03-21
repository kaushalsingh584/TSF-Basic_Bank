from django.contrib import admin

# Register your models here.
from transactions.models import Customer,Transaction

admin.site.register(Customer)
admin.site.register(Transaction)
