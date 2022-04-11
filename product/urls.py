
from django.urls import  path
from .views import *
app_name="product"
urlpatterns = [ 
    path('',list_product_view,name="product_list"),
    path('create-product',create_product_view,name="product_create"),
    path('delete-product/<int:id>',delete_product_view,name="product_delete")
]

