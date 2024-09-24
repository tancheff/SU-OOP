from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    def __init__(self, name: str, price: float):
        self.portion = 250
        super().__init__(name, self.portion, price)

    def details(self) -> str:
        return f"Stolen {self.name}: 250g - {self.price:.2f}lv."