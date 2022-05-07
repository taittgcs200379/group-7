from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("category/", views.category_index),
    path("category/<int:id>", views.category_details),
    path("category/add", views.category_add),
    path("category/delete/<int:id>", views.category_delete),
    path("category/edit/<int:id>", views.category_edit),
    path("category/back_to_categorylist", views.back_to_categorylist),
    path("category/edit/back_to_categorylist", views.back_to_categorylist),
    path("store/", views.store_index),
    path("store/<int:id>", views.store_details),
    path("store/add", views.store_add),
    path("store/delete/<int:id>", views.store_delete),
    path("store/edit/<int:id>", views.store_edit),
    path("store/back_to_storelist", views.back_to_storelist),
    path("store/edit/back_to_storelist", views.back_to_storelist),
    path("store/details/<int:id>", views.store_details),
    path("store/details/back_to_storelist", views.back_to_storelist),   
    path("store/show_category/<int:category_id>", views.show_category)
]

    
