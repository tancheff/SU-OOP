from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    def __init__(self):
        self.protection = 120
        self.price = 15
        super().__init__(protection=self.protection, price=self.price)

    def increase_price(self) -> None:
        self.price *= 1.2
