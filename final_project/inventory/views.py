from django.shortcuts import render
from django.urls import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import Group, Permission

from .models import Product, Customer, Purchase, Stock, products_purchase
from .forms import ProductForm, PurchaseForm, CustomerForm, StockForm, Products_PurchaseForm

from datetime import datetime
import re

# Create your views here.
@login_required()
def index(request):
  
    return render(request, 'inventory/index.html', {
        'products': Product.objects.all(), 'customers': Customer.objects.all(),
        'purchases': Purchase.objects.all(), 'stocks': Stock.objects.all(),
    })

# READ
@login_required()
def products(request):
    return render(request, 'inventory/products.html', {'products': Product.objects.all()})

@login_required()
def customers(request):
    return render(request, 'inventory/customers.html', {'customers': Customer.objects.all()})

@login_required()
def stocks(request):
    return render(request, 'inventory/stocks.html', {'stocks': Stock.objects.all()})

@login_required()
def purchases(request):
    return render(request, 'inventory/purchases.html', {'purchases': Purchase.objects.all()})  

# UPDATE
@login_required()
def update_product(request,product_id):
    product = Product.objects.get(pk=product_id)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('inventory:index'))
    
    context = {'product': product, 'form': form}
    return render(request, 'inventory/view_product.html', context)

@login_required()
def update_customer(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        customer.firstname = request.POST.get('firstname')
        customer.lastname = request.POST.get('lastname')
        customer.save()
        return HttpResponseRedirect(reverse('inventory:index'))

    context = {'customer': customer, 'form':form}
    return render(request, 'inventory/view_customer.html', context)

@login_required()
def update_purchase(request, purchase_id):
    items = products_purchase.objects.filter(purchase=purchase_id).all()
    
    context = {'items': items, 'purchase': purchase_id, 'customers': Customer.objects.all(),}
    return render(request, 'inventory/view_purchase.html', context)

@login_required()
def update_stock(request, stock_id):
    stock = Stock.objects.get(pk=stock_id)
    form = StockForm(instance=stock)

    context = {'stock': stock, 'form':form}
    return render(request, 'inventory/view_stock.html', context)

# CREATE
@login_required()
def create_product(request):
    form =ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('inventory:products'))
        
    context = {'form':form}
    return render(request, 'inventory/add.html', context)

@login_required()
def create_customer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('inventory:customers'))

    context = {'form':form}
    return render(request, 'inventory/add.html', context)

@login_required()
def create_purchase(request):
    if request.method == 'POST':
        customer = Customer.objects.get(pk=request.POST.get('customer'))
        products = request.POST.getlist('product')
        qtys = request.POST.getlist('qty')
        purchase = Purchase()
        purchase.customer = customer
        purchase.save()

        for idx in range(0,len(products)):
            product = Product.objects.get(pk=products[idx])
            
            purchase_item = products_purchase()
            purchase_item.purchase = purchase
            purchase_item.product = product
            purchase_item.qty = qtys[idx]
            purchase_item.selling_price = product.price
            purchase_item.save()

            stock = Stock()
            stock.product = product
            stock.qty_out = qtys[idx]
            stock.description = 'sale'
            stock.products_purchase = purchase_item
            stock.price = product.price
            stock.save()

        return HttpResponseRedirect(reverse('inventory:purchases'))

    context = {'customers': Customer.objects.all(), 'now': datetime.now(),
                'products': Product.objects.all(), 
    }
    return render(request, 'inventory/add_purchase.html', context)

@login_required()
def create_stock(request):
    form = StockForm()
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('inventory:stocks'))

    context = {'form':form}
    return render(request, 'inventory/add.html', context)

# DELETE
@login_required()
def delete_product(request, id):
    product = Product.objects.get(pk=id)
    product.delete()

    return HttpResponseRedirect(reverse('inventory:products'))

@login_required()
def delete_customer(request, id):
    customer = Customer.objects.get(pk=id)
    customer.delete()

    return HttpResponseRedirect(reverse('inventory:customers'))

@login_required()
def delete_stock(request, id):   
    stock = Stock.objects.get(pk=id)
    if stock.products_purchase == None:
        stock.delete()
    
    return HttpResponseRedirect(reverse('inventory:stocks'))

@login_required()
def invoice(request, purchase_id):
    items = products_purchase.objects.filter(purchase=purchase_id).all()

    context = {'items' : items, 'purchase_id': purchase_id}
    return render(request, 'inventory/invoice.html', context)

# PRICE FETCHER
def fetch_price(request, product_id):
    product = Product.objects.get(pk=product_id)
    if product:
        return HttpResponse(product.price)
    else:
        raise Http404('Cannot find price!!') 