# Create your views here.
from django.shortcuts import render, redirect
from .forms import BillingForm, ProductFormSet
from .models import Product, Transaction
from django.db import transaction
from django.utils import timezone
from django.utils.dateparse import parse_datetime

def billing_page(request):
    if request.method == 'POST':
        billing_form = BillingForm(request.POST)
        product_formset = ProductFormSet(request.POST)

        if billing_form.is_valid() and product_formset.is_valid():
            customer_email = billing_form.cleaned_data['customer_email']
            cash_paid = billing_form.cleaned_data['cash_paid']
            denominations = {key: billing_form.cleaned_data[key] for key in billing_form.fields if 'denomination' in key}

            total_price = 0
            transaction_date = timezone.now().replace(microsecond=0)  # Truncate microseconds
            
            # Start a database transaction to ensure atomicity
            with transaction.atomic():
                # Iterate over each product form and process it
                for product_form in product_formset:
                    product_id = product_form.cleaned_data.get('product_id')
                    quantity = product_form.cleaned_data.get('quantity')
                    
                    # Retrieve the product details
                    product = Product.objects.get(product_id=product_id)
                    
                    # Calculate the purchase price and tax
                    purchase_price = product.unit_price * quantity
                    tax = (purchase_price * product.tax_percentage) / 100
                    total_price += purchase_price + tax  # Accumulate total price

                    # Create the transaction record for this product
                    Transaction.objects.create(
                        customer_email=customer_email,
                        product_id=product_id,
                        quantity=quantity,
                        purchase_price=purchase_price,
                        tax_amount=tax,
                        total_price=total_price,
                        date=transaction_date,  # Store the transaction time
                        **denominations,  # Add the denominations to the transaction
                        cash_paid=cash_paid
                    )
            
            # Redirect to the receipt page, passing the transaction date_time to fetch the details
            return redirect('receipt_page', date_time=transaction_date)

    else:
        # Initialize empty forms for GET requests
        billing_form = BillingForm()
        product_formset = ProductFormSet()

    return render(request, 'billing_page.html', {
        'billing_form': billing_form,
        'product_formset': product_formset
    })

def calculate_denominations(balance):
    denominations = [500, 50, 20, 10, 5, 2, 1]  # Available denominations
    breakdown = {}

    for denom in denominations:
        count = balance // denom  # Calculate the number of notes/coins of this denomination
        if count > 0:
            breakdown[denom] = count
        balance %= denom  # Update the balance to the remainder after using this denomination

    return breakdown
    
def receipt_page(request,date_time):
    # Retrieve the relevant transaction and related details
    date_time = parse_datetime(date_time)
    
    transactions = Transaction.objects.filter( 
        date__year=date_time.year,
        date__month=date_time.month,
        date__day=date_time.day,
        date__hour=date_time.hour,
        date__minute=date_time.minute)

    total_amount = sum([transaction.purchase_price + transaction.tax_amount for transaction in transactions])
    cash_paid = transactions.first().cash_paid if transactions else 0

    # Calculate balance and its denomination breakdown
    balance = cash_paid - total_amount
    denomination_breakdown = calculate_denominations(balance)

    return render(request, 'receipt_page.html', {
        'transactions': transactions,
        'total_amount': total_amount,
        'cash_paid': cash_paid,
        'balance': balance,
        'denomination_breakdown': denomination_breakdown,
    })