from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    product_id = models.CharField(max_length=50, unique=True)
    available_stock = models.IntegerField()
    unit_price = models.FloatField()
    tax_percentage = models.FloatField()

    def __str__(self):
        return self.name

class Transaction(models.Model):
    customer_email = models.EmailField()
    product_id = models.CharField(max_length=50)
    quantity = models.IntegerField()
    purchase_price = models.FloatField()
    tax_amount = models.FloatField()
    total_price = models.FloatField()
    denomination_500 = models.IntegerField(default=0)
    denomination_50 = models.IntegerField(default=0)
    denomination_20 = models.IntegerField(default=0)
    denomination_10 = models.IntegerField(default=0)
    denomination_5 = models.IntegerField(default=0)
    denomination_2 = models.IntegerField(default=0)
    denomination_1 = models.IntegerField(default=0)
    cash_paid = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Truncate microseconds before saving to database
        if self.date:
            self.date = self.date.replace(microsecond=0)
        super().save(*args, **kwargs)
