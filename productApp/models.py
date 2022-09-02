from tkinter import CASCADE
from django.db import models
from django.utils import timezone
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator 
from productApp.choices import ORDER_STATUS_CHOICES, orderStatus


class Product(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, null=False)
    title = models.CharField(max_length=150,blank=False)
    price = models.IntegerField(blank=False, null=False)
    seller = models.ForeignKey('usersApp.User' , on_delete=models.CASCADE)

    class Meta:
        ordering = ['price']
    def __str__(self):
        return str(self.title)

class cartItem(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    itemPrice = models.IntegerField(default=0)
    cart = models.ForeignKey('cart',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product.title)


class Cart(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, null=False)
    items = models.ManyToManyField(cartItem , related_name='+')
    created_at = models.DateTimeField('created at', default=timezone.now)
    modified_at = models.DateTimeField('modified at', default=timezone.now)

    

    def __str__(self):
        return str(self.uuid)

        
        
class checkOut(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, null=False)
    user = models.ForeignKey('usersApp.User' , on_delete=models.CASCADE)
    items = models.ManyToManyField(cartItem)
    totalPrice = models.IntegerField()
    status = models.CharField('Status', choices=ORDER_STATUS_CHOICES, default=orderStatus.PENDING ,max_length=128)
    address = models.CharField(max_length=300, null=False, blank=False)    