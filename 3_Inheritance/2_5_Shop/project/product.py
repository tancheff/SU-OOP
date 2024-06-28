class Product:
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def decrease(self, quantity: int) -> None:
        if self.quantity >= quantity:
            self.quantity -= quantity

    def increase(self, quantity: int) -> None:
        self.quantity += quantity

    def __repr__(self) -> str:
        return self.name


# decrease(quantity: int) - decreases the quantity of the product only if there is enough
# increase(quantity: int) - increases the quantity of the product
# __repr__() - override the method, so it returns the name of the product