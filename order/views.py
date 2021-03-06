from rest_framework import viewsets, mixins, permissions, views

from .models import Order 
from .serializers import OrderSerializer
from .permissions import IsOwner
import stripe 




class OrderViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsOwner, ]

    def get_queryset(self):
        user = self.request.user 
        return Order.objects.filter(user=user)

