from django.shortcuts import render
from .models import *


def index(request):
    # quantity = 3
    # dish = Dish.objects.get(id='2')
    # price = Dish.objects.get(id='2').price * quantity
    # order = Order.objects.create(price=price, dish=dish, quantity=3)
    # order.save()
    orders = Order.objects.all()
    return render(request, 'delivery/index.html', context={'orders': orders})
