from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Vegetables', 'Vegetables'),
        ('Fruits', 'Fruits'),
        ('Meat', 'Meat'),
        ('Fish', 'River Fish'),
        ('Spices', 'Spices'),
    ]

    name = models.CharField(max_length=30)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Vegetables')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name
