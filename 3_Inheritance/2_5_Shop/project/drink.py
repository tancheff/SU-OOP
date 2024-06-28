from project.product import Product


class Drink(Product):
    def __init__(self, name: str, quantity: int = 10):
        super().__init__(name, quantity)


# In the file drink.py, the class Drink should be implemented.
# The class should inherit from the Product class.
# An instance of the Drink class will have a name and a quantity of 10.
