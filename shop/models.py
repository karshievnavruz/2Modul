from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    year = models.PositiveIntegerField()  # Yil
    memory = models.PositiveIntegerField(help_text="GB")  # Xotira (GB)
    
    CONDITION_CHOICES = [
        ('new', 'Yangi'),
        ('used', 'Ishlatilgan'),
        ('refurbished', 'Ta’mirlangan'),
    ]
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)

    def __str__(self):
        return self.name
