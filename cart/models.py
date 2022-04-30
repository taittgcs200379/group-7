
from django.db import models
from django.contrib.auth.models import User
from shop.models import Store


# Create your models here.
class Cart(models.Model):
    User = models.ForeignKey(User , on_delete=models.CASCADE, blank= True, null=True)
    

    def __str__(self):
        return "Cart_" + str(self.User)

class CartItems(models.Model):
    Quantity = models.IntegerField()
    Store= models.ForeignKey(Store, on_delete=models.CASCADE)
    Cart=models.ForeignKey(Cart, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Cart}_{self.Store}"
    
class Order(models.Model):
    Order_date=models.DateTimeField()
    User = models.ForeignKey(User , on_delete=models.CASCADE, blank= True, null=True)

    def __str__(self):
        return f"Order_{str(self.id)} ({str(self.User)})"
class Orderitems(models.Model):
    Quantity=models.IntegerField()
    Store = models.ForeignKey(Store, on_delete=models.CASCADE)
    Price = models.FloatField()
    Order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.Order}_{self.Store}"  
    
    
    