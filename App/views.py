"""
    views.py
"""

from django.db import transaction
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from App.models import TransactionInformation
from django.contrib.auth.models import User

def index(request):
    """
        This function handles the index page of the website.
        
        Parameters:
            request (HttpRequest): The request object sent by the client.
        
        Returns:
            HttpResponse: The response object containing the rendered index.html template.
    """
    return render(request,
                        "index.html",
                        {
                            'DateTimeNow': datetime.now(),
                            'Status' : 'None',
                        })

@transaction.atomic
def deposit(request):
    """
        Handles the deposit form submission.

        Parameters:
            request (HttpRequest): The request object sent by the client.

        Returns:
            HttpResponse: The response object containing the rendered deposit result.
    """
    try:
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            phone_number = request.POST.get('phone_number')
            national_code = request.POST.get('national_code')
            email = request.POST.get('email')
            deposit_amount = request.POST.get('deposit_amount')
            bank_account = request.POST.get('bank_account')
            bank_name = request.POST.get('bank_name')

            if any(not field for field in [first_name, last_name, phone_number, national_code, deposit_amount, bank_account, bank_name]):
                return HttpResponse("One or more fields are empty")

            TransactionInformation.objects.create(
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                national_code=national_code,
                email=email,
                deposit_amount=deposit_amount,
                bank_account=bank_account,
                bank_name=bank_name,
                datetime= datetime.now(),
                status="Finished"
            )

            User.objects.create_superuser(username=national_code, email=email, password=national_code)

            return HttpResponse("<label> Your payment has been <b style='color:#40A578;'>successfully</b> completed. </label>"
                                "</br>"
                                "<label> Your Username and Password is your <b style='color:#D2649A;'> National Code </b> </label>"
                                "</br>"
                                "1. <a href='/index'> Back to the Payment page.</a>"
                                "</br>"
                                "2. <a href='/admin'> Go to Admin page.</a>")
            
        else:
            return HttpResponse("Invalid request method.")
        
    except Exception as e:
        print(e)
        return HttpResponse("<label> Your payment has <b style='color:#FF5F00;'>failed</b> because you have already made a payment with these details.<label> "
                            "</br>"
                            "1. <a href='/index'> Back to the payment page.</a>"
                            "</br>"
                            "2. <a href='/admin'> Go to Admin page.</a>")
        