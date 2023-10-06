from django.db import models
from users.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}"


class Lectures(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True)
    watchnig_time = models.DurationField()

    def __str__(self) -> str:
        return f"{self.name}"
