from django.db import models

# Create your models here.
from django.db import models
from apps.orders.models import Order  
from apps.products.models import Product 

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def verifica_total(self):
        total = self._unitary_price * self._quantity
        return total