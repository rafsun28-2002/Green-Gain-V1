from django.db import models

class OrderInfo(models.Model):  # ✅ Inherit from models.Model
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    street = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

class Checkout(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    notes = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"


