from django.contrib import admin
from .models import Product, Transaction

# Register Product model
admin.site.register(Product)

# Register Transaction model
admin.site.register(Transaction)