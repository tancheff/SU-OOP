from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    def __init__(self):
        self.protection = 90
        self.price = 25
        super().__init__(protection=self.protection, price=self.price)

    def increase_price(self) -> None:
        self.price *= 1.1
