from django import forms

from .models import Product, Purchase, Customer, Stock, products_purchase


form_class = 'form-control'
form_style = 'max-width:50%;'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': form_class, 'style': form_style}),
            'price': forms.NumberInput(attrs={'class': form_class, 'style': form_style}),
        }

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['customer','discount'] 
        widgets = {
            'customer' : forms.TextInput(attrs={'class': form_class, 'style': form_style}),
             'discount': forms.NumberInput(attrs={'class': form_class, 'style': form_style}),
        }   

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        widgets = {
            'firstname': forms.TextInput(attrs={'class': form_class, 'style': form_style}),
            'lastname': forms.TextInput(attrs={'class': form_class, 'style': form_style}),
            'phone' : forms.TextInput(attrs={'class': form_class, 'style': form_style})
        }
        
class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['product','qty_in','description','price']
        widgets = {
            'product' : forms.Select(attrs={'class': form_class, 'style': form_style}),
            'qty_in' : forms.NumberInput(attrs={'class': form_class, 'style': form_style}),
            'description': forms.TextInput(attrs={'class': form_class, 'style': form_style}),
            'price' : forms.NumberInput(attrs={'class': form_class, 'style': form_style})
        }        

class Products_PurchaseForm(forms.ModelForm):
    class Meta:
        model = products_purchase
        fields = '__all__'
