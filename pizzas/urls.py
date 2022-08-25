"""Defines URL patterns for pizzas."""

from django.urls import path
from . import views

app_name = "pizzas"

urlpatterns = [
    # Home page
    path("", views.index, name="index"),
    # Page that shows all pizzas.
    path("pizzas/", views.pizzas, name="pizzas"),
    # Detail page for a single pizza.
    path("pizzas/<int:my_pizza_id/", views.my_pizza, name="my_pizza"),
]
