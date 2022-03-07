from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Customer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phone = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True)

    def __str__(self):
        return f'{self.firstname} {self.lastname}, ({self.phone})'

class Product(models.Model):
    name = models.CharField(max_length=55)
    price = models.FloatField()
    image = models.ImageField(null=True, default='default.jpg')

    # property to return stock levels (all in - all out) (derived attr)
    @property
    def qty_in_stock(self):
        self.pk # use this as the id
        row = Stock.objects.filter(product_id=self.pk).all()
        qty_in = [obj.qty_in for obj in row]
        qty_out = [obj.qty_out for obj in row] 
        return sum(qty_in)-sum(qty_out)

    def __str__(self):
        return f'{self.name}'

class Purchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='purchases')
    date = models.DateTimeField(auto_now_add=True, blank=True)
    discount = models.FloatField(blank=True, null=True)
    product_list = models.ManyToManyField(Product, through='products_purchase', blank=True)

    # attribute to return sum of qty for all items in purchase
    @property
    def total_qty(self):
        items = products_purchase.objects.filter(purchase=self).all()
        qty = [item.qty for item in items]
        return sum(qty)

    # attribute to return sum of price for all items in purchase
    @property
    def total_price(self):
        items = products_purchase.objects.filter(purchase=self).all()
        amount = [item.amount for item in items]
        return sum(amount)

    def __str__(self):
        return f'{self.pk}) {self.customer} ({self.date})'


class products_purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sales')
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name='products')
    qty = models.IntegerField(default=1)
    selling_price = models.FloatField()

    @property
    def unit_price(self):
        return self.product.price

    @property
    def amount(self):
        return (self.unit_price*self.qty)
    
    # class for specifying row unique values (prevents duplicates)
    class Meta:
        unique_together = [['product','purchase']]

    def __str__(self):
        return f'{self.pk}) {self.product}, {self.purchase}'

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inventory')
    qty_in = models.IntegerField(blank=True, default=0)
    qty_out = models.IntegerField(blank=True, default=0)
    description = models.CharField(max_length=100)
    products_purchase = models.OneToOneField(products_purchase,blank=True, null=True, on_delete=models.CASCADE, related_name='stockout')
    date = models.DateTimeField(auto_now_add=True, blank=True)
    price = models.FloatField(blank=True)

    def __str__(self):
        return f'{self.pk}) {self.product}, {self.qty_in}, {self.qty_out}, {self.description}, {self.date}'
