from equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    def __init__(self):
        super().__init__(120, 15)

    def increase_price(self):
        self.price = self.price * 1.2

