"""
from django import forms
from .models import Conglomerate, Cert, Product


class OrderForm(forms.ModelForm):

    class Meta:
        model = Orders
        fields = ('customer', 'order_date', 'order_slot', 'order_details',)
"""
