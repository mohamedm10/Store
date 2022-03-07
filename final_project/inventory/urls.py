from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.index, name="index"),

    path('product/<product_id>', views.update_product, name='update_product'),
    path('customer/<customer_id>', views.update_customer, name='update_customer'),
    path('purchase/<purchase_id>', views.update_purchase, name='update_purchase'),
    path('stock/<stock_id>', views.update_stock, name='update_stock'),

    path('add-product', views.create_product, name='create_product'),
    path('add-customer', views.create_customer, name='create_customer'),
    path('add-purchase', views.create_purchase, name='create_purchase'),
    path('add-stock', views.create_stock, name='create_stock'),

    path('all-products', views.products, name='products'),
    path('all-customers', views.customers, name='customers'),
    path('all-stocks', views.stocks, name='stocks'),
    path('all-purchases', views.purchases, name='purchases'),

    path('del-product/<id>', views.delete_product, name='delete_product'),
    path('del-customer/<id>', views.delete_customer, name='delete_customer'),
    path('del-stock/<id>', views.delete_stock, name='delete_stock'),

    path('invoice/<purchase_id>', views.invoice, name='invoice'),

    path('fetch_price/<product_id>', views.fetch_price, name='fetch_price'),
]