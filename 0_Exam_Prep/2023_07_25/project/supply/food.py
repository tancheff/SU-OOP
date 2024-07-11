from project.supply.supply import Supply


class Food(Supply):
    def __init__(self, name: str, energy: int = 25):
        super().__init__(name, energy)
        self.type = "Food"

    def details(self) -> str:
        # return f"{self.type}: {self.name}, {self.energy}"
        return f"Food: {self.name}, {self.energy}"
