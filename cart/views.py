

from datetime import datetime

from django.shortcuts import redirect, render

from shop.views import store_index
from .models import CartItems, Cart, Order, Orderitems
from shop.models import Store


# Create your views here.from shop.models import Store

def add_to_cart(request, store_id):
    cart = Cart.objects.get(id=1)
    store = Store.objects.get(id=store_id)

    cart_item= CartItems.objects.filter(Store=store, Cart=cart).first()
    if cart_item is None:    
       store=Store.objects.get( id = store_id )


       cart = Cart.objects.get(id=1)
       cart_item= CartItems()
       cart_item.Store=store
       cart_item.Cart=cart
       cart_item.Quantity= 1
       cart_item.save() 
    else:
       cart_item.Quantity += 1
       cart_item.save()

    return redirect(store_index) 


def remove(request, store_id):
     cart = Cart.objects.get(id=1)
     store = Store.objects.get(id=store_id)
     cart_item= CartItems.objects.filter(Store=store, Cart=cart).first()

     if cart_item is not None:
        cart_item.delete()

     return redirect(show_cart)   


def show_cart(request):
   if request.method =="POST":
      cart = Cart.objects.get(id=1)
      store = Store.objects.get(id = request.POST["store_id"])

      cart_item= CartItems.objects.filter(Store=store, Cart=cart).first()

      if cart_item is not None:
         cart_item.Quantity=request.POST["quantity"]
         cart_item.save()

   cart = Cart.objects.get(id=1)
   cart_items= CartItems.objects.filter(Cart=cart)

   context ={
      "cart_items": cart_items,
   }

   return render(request, "index.html", context)

def order(request):
     cart = Cart.objects.get(id=1)

     cart_items= CartItems.objects.filter(Cart=cart)

     if cart_items:
        order = Order()
        order.Order_date =datetime.now()

        order.save()

        for item in cart_items:
            order_item =Orderitems()
            order_item.Store = item.Store
            order_item.Quantity = item.Quantity
            order_item.Price= item.Store.price
            order_item.Order = order

            order_item.save()
            item.delete()
     return render(request, "order_success.html")

def order_history(request):
    orders = Order.objects.filter(User= None)

    context = {
       "orders": orders,
    }
    return render(request, "order_history.html", context)     

def order_details(request, order_id):
   order = Order.objects.get(id=order_id)
   order_items= Orderitems.objects.filter(Order=order)
   context={
      "order_items": order_items

   }
   return render(request, "order_details.html", context)   