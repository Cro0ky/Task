from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    category = models.ManyToManyField('Category')

    def __str__(self):
        return self.name


class Order(models.Model):
    price = models.PositiveIntegerField()
    dish = models.ForeignKey('Dish', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'Заказ - {self.dish}'
