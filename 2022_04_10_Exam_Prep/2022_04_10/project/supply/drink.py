from project.supply.supply import Supply


class Drink(Supply):
    INITIAL_ENERGY = 15

    def __init__(self, name: str):
        super().__init__(name, Drink.INITIAL_ENERGY)
        self.type = "Drink"

    def details(self) -> str:
        # return f"{self.type}: {self.name}, {self.energy}"
        return f"Drink: {self.name}, {self.energy}"
