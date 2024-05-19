from django.db import models

class Payment(models.Model):
    order = models.OneToOneField('orders.Order', on_delete=models.CASCADE)
    payment_gateway_transaction_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Order #{self.order.id}"
