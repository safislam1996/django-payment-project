import json
import re
from unicodedata import decimal, name
from django.dispatch import receiver
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import decimal
from django.views.decorators.csrf import csrf_exempt
from pkg_resources import require
from payment.form import Transaction
from .models import Customer
from django.db import transaction
# Create your views here.

@csrf_exempt
def home(request):

    if request.method == 'POST':

        form= Transaction(request.POST)

        if form.is_valid():

            sender=form.cleaned_data['sender']
            receiver=form.cleaned_data['receiver']
            change=decimal.Decimal(form.cleaned_data['amount'])

            
        with transaction.atomic():
            input_1=Customer.objects.select_for_update().get(name=sender)
            input_2=Customer.objects.select_for_update().get(name=receiver)
        
            input_1.balance-=change
            input_1.save()

            input_2.balance+=change
            input_2.save()

            return HttpResponseRedirect('/success')


    else:
        form=Transaction()
        # print(form)
   
    return render(request,'home.html',{'form':form})










def success_page(request):
    users=Customer.objects.all()
    return render(request,'success.html',{'users':users})