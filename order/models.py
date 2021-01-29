from django.db import models
from django.contrib.auth import get_user_model

from product.models import Product


ORDER_STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('processing', 'Processing'),
    ('in_delivery', 'In delivery'),
    ('finished', 'Finished'),
    ('canceled', 'Canceled'),
)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_total_price(self):
        return self.quantity * self.product.price

    def get_final_price(self):
        return self.get_total_price()

class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='orders', null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES)
    address = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    items = models.ManyToManyField(OrderItem)
    paid = models.BooleanField(default=False)


    def get_total(self):
        total = 0 
        for item in self.items.all():
            total += item.get_final_price()
            return total
