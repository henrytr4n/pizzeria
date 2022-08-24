from django.db import models

# Create your models here.
class Pizza(models.Model):
    """A pizza with a name"""

    name = models.CharField(max_length=20)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name


class Topping(models.Model):
    """Pizza toppings"""

    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
        """Return a string representation of the model."""
        return self.name
