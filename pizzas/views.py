from django.shortcuts import render
from .models import Pizza

# Create your views here.
def index(request):
    """The home page for Pizzeria."""
    return render(request, "pizzas/index.html")


def pizzas(request):
    """Show all pizzas."""
    pizzas = Pizza.objects.all()
    context = {"pizzas": pizzas}
    return render(request, "pizzas/pizzas.html", context)


def my_pizza(request, pizza_id):
    """Show my pizza."""
    my_pizza = Pizza.objects.get(id=pizza_id)
    toppings = my_pizza.topping_set.all()
    context = {"my_pizza": my_pizza, "toppings": toppings}
    return render(request, "pizzas/my_pizza.html", context)
