from django.urls import path
from . import views

urlpatterns = [
    path('', views.billing_page, name='billing_page'),
    path('billing/receipt/<str:date_time>/', views.receipt_page, name='receipt_page'),
]
