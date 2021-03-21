from django.shortcuts import render
from .models import Customer,Transaction

template_name = 'transfer.html'
# Create your views here.
def home(request):
    return render(request,"index.html")

def customer(request):
    custs = Customer.objects.all()

    return render(request,"customers.html",{'data':custs})

def transfer(request):
    
    custs = Customer.objects.all()
    
    return render(request,"transfer.html",{'data':custs})

def transop(request):
    if request.method  == 'POST':
        cred_to = request.POST["transfer_to"]
        debt_from =  request.POST["transfer_from"]
        amount = request.POST["amount"]
        try:
            receiver = Customer.objects.get(account_number= cred_to)
            sender = Customer.objects.get(account_number= debt_from)
            amount = int(amount)
            if amount <= sender.balance:
                
                sender.balance -= amount
                receiver.balance += amount
                sender.save()
                receiver.save()
                new_txn = Transaction(
                    debited_from=sender, credited_to=receiver, amount=amount,  transaction_status="SUCCESS")
                new_txn.save()
                data = Transaction.objects.all().order_by('-transaction_date')
                context={'data':data,'message': "Transaction successful."}        
                return render(request,"transactions.html" , context)
                    
            
            
            else:
                new_txn = Transaction(
                    debited_from=sender, credited_to=receiver, amount=amount,  transaction_status="FAILED")
                new_txn.save()
                custs = Customer.objects.all()
                return render(request, template_name, {'data':custs,'error': "Account doesn't have sufficient balance."})
        except Customer.DoesNotExist:
            return render(request, template_name, {"error": "Account Number does not match with any customer."})

    else:
        return render(request, template_name)


def transaction_table(request):
    data = Transaction.objects.all().order_by('-transaction_date')
    context={'data':data}
    return render(request,"transactions.html",context)