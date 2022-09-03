from django.db import models
from datetime import datetime
from products.models import Product
from user.models import User

# Create your models here.
class Orders(models.Model):
    created_at = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
class OrderItems(models.Model):
    order = models.ForeignKey(Orders,related_name='orderitems',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    @property
    def total_amount(self):
        return f"quantity is:{self.quantity} total price is:{self.quantity*self.product.price}"
    
    def __str__(self):
        return self.product.name +" " +str(self.total_amount)