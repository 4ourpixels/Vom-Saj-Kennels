from django.db import models


class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    age = models.DateField()
    age = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='dogs')

    def __str__(self):
        return self.name
