from dataclasses import fields
from django import forms
from django.dispatch import receiver
from .models import Customer


class Transaction(forms.Form):
    sender=forms.CharField(max_length=30)
    receiver=forms.CharField(max_length=30)
    amount=forms.CharField(max_length=30)

