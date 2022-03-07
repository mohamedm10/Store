from ssl import SSLSocket
from django.contrib import admin
from .models import Customer, Product, Purchase, Stock, products_purchase

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','qty_in_stock']

@admin.register(products_purchase)
class Products_PurchaseAdmin(admin.ModelAdmin):
    list_display = ['product','purchase','unit_price']

admin.site.register(Customer)
# admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(Stock)
# admin.site.register(products_purchase)