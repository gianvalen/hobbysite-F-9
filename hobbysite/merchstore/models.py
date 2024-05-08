from django.db import models
from django.urls import reverse

from user_management.models import Profile

class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('merchstore:items', args=[self.pk])

    class Meta:
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, related_name="owner")
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    stock = models.PositiveIntegerField()

    STATUS_CHOICES = (
        ('Available', 'Available'),
        ('On Sale', 'On Sale'),
        ('Out of Stock', 'Out of Stock')
    )

    stock_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Available')
    product_type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True, related_name="items")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('merchstore:item', args=[self.pk])

    def save(self, *args, **kwargs):
        if self.stock == 0:
            self.stock_status = 'Out of Stock' 
        elif self.stock > 0 and self.stock_status == 'Out of Stock':
            self.stock_status = 'Available'   
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['product_type', 'name']


class Transaction(models.Model):
    buyer = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name="buyer")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="product")
    amount = models.PositiveIntegerField()

    TRANSACTION_CHOICES = (
        ('On Cart', 'On Cart'),
        ('To Pay', 'To Pay'),
        ('To Ship', 'To Ship'),
        ('To Receive', 'To Receive'),
        ('Delivered', 'Delivered')        
    )

    transaction_status = models.CharField(max_length=20, choices=TRANSACTION_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)