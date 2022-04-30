from django.contrib import admin

from cart.models import Cart, CartItems, Order, Orderitems

# Register your models here.
admin.site.register(Cart)
admin.site.register(CartItems)
admin.site.register(Order)
admin.site.register(Orderitems)



