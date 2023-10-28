from django.db import models
from users.models import CustomUser


CATEGORY_CHOICES = (
    ('BOOKS', 'books'),
    ("CLOTHES", "clothes"),
    ("TECHNIQUES", "techniques"),
    ("PHONES", "phones"),
    ("COMPUTERS", "computers"),

)



class Product(models.Model):
    name = models.CharField(max_length=100)
    old_price = models.FloatField()
    new_price = models.FloatField()
    description = models.TextField()
    product_image = models.ImageField(null=True, blank=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100)
    digital = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return self.name



class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    data_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction = models.CharField(max_length=20, null=True)

    def __str__(self):
        return str(self.id)



class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address









































