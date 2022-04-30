from django.contrib import admin

from cart.models import Cart, CartItems


from .models import Category, Store

# Register your models here.
class StoreAdmin(admin.ModelAdmin):
    list_display=('name','image','code','id','date')
    search_fields=['name']
    list_filter = ('code','image','id','date')
admin.site.register(Store, StoreAdmin) 
admin.site.register(Category)



