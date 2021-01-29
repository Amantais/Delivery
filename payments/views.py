from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
import json
from django.conf import settings

import stripe
from rest_framework.decorators import api_view
from rest_framework import views 
from order.models import Order



stripe.api_key = settings.STRIPE_SECRET_KEY



@api_view(['POST'])
def create_payment_intent(request, order_id):
    try:
        order_instance = Order.objects.get(id=order_id)
        order_in_total = int(order_instance.total * 100)
        order_instance.status = 'in_delivery'
        order_instance.save()
        intent = stripe.Charge.create(
            amount=request.POST.get('amount', order_in_total),
            currency=request.POST.get('currency', 'USD'),
            source=request.POST.get('source', ''),
            description=request.POST.get('description', ''),
            metadata={'order_id': 12345},
        )
        content = json.dumps({'client_secret': intent['client_secret']})

        return HttpResponse(json.dumps(
            {'message': 'Your transactions has been successful.'})
        )
    except Exception:
        return HttpResponse(json.dumps(
            {'message': 'Your transaction has been successful.'})
        )


