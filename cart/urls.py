from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
   path("add_to_cart/<int:store_id>", views.add_to_cart),   
   path("remove/<int:store_id>", views.remove),   
   path("main",views.show_cart),
   path("order_success",views.order),
   path("history",views.order_history),
   path("order_details/<int:order_id>",views.order_details),
]
