# Generated by Django 5.1.3 on 2024-11-24 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('product_id', models.CharField(max_length=50, unique=True)),
                ('available_stock', models.IntegerField()),
                ('unit_price', models.FloatField()),
                ('tax_percentage', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_email', models.EmailField(max_length=254)),
                ('product_id', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('purchase_price', models.FloatField()),
                ('tax_amount', models.FloatField()),
                ('total_price', models.FloatField()),
                ('denomination_500', models.IntegerField(default=0)),
                ('denomination_50', models.IntegerField(default=0)),
                ('denomination_20', models.IntegerField(default=0)),
                ('denomination_10', models.IntegerField(default=0)),
                ('denomination_5', models.IntegerField(default=0)),
                ('denomination_2', models.IntegerField(default=0)),
                ('denomination_1', models.IntegerField(default=0)),
                ('cash_paid', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]