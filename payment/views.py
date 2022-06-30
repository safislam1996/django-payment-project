import re
from unicodedata import name
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from payment.form import Transaction
from .models import Customer
# Create your views here.


def home(request):

    if request.method =='POST':
        form=Transaction(request.POST)

        if form.is_valid():
            print(form.cleaned_data)

        return HttpResponseRedirect('/')

    else:
        form=Transaction()

    return render(request,'home.html',{'form':form})


# def get_payment(request):
#     if request.method=='POST':
#         return form
#     else:
    
#     return render(request,'home.html',{'form':form})