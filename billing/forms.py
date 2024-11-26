from django import forms
from .models import Product
from django.forms import formset_factory

class ProductForm(forms.Form):
    product_id = forms.CharField(label="Product ID")
    quantity = forms.IntegerField(min_value=1, label="Quantity")

ProductFormSet = formset_factory(ProductForm, extra=1)


class BillingForm(forms.Form):
    customer_email = forms.EmailField(label="Customer Email")
    cash_paid = forms.FloatField(label="Cash Paid by Customer")
    denomination_500 = forms.IntegerField(initial=0, label="500")
    denomination_50 = forms.IntegerField(initial=0, label="50")
    denomination_20 = forms.IntegerField(initial=0, label="20")
    denomination_10 = forms.IntegerField(initial=0, label="10")
    denomination_5 = forms.IntegerField(initial=0, label="5")
    denomination_2 = forms.IntegerField(initial=0, label="2")
    denomination_1 = forms.IntegerField(initial=0, label="1")
