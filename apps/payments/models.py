from django.db import models
from orders.models import models
from orders.models import Order
# Create your models here.
class Payment(models.Model):
    payment_date = models.DateField('Data do Pagamento')
    amount = models.FloatField('Valor Pago')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="payments")

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
        ordering = ['payment_date']

    def __str__(self):
        return f"Pagamento de R$ {self.amount:.2f} - Pedido {self.order.id}"