from project.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    def __init__(self, name: str, price: float):
        self.portion = 200
        super().__init__(name, self.portion, price)

    def details(self) -> str:
        return f"Gingerbread {self.name}: 200g - {self.price:.2f}lv."
