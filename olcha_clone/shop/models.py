from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)  # Mahsulot nomi
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Narx
    description = models.TextField()  # Tavsif

    def __str__(self):
        return self.name  # Mahsulot nomi ko'rsatiladi
