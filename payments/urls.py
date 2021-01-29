from django.urls import path

from .views import  create_payment_intent

urlpatterns = [
    path('create/payment/<int:order_id>/', create_payment_intent, name='create-payment-intent'),
]