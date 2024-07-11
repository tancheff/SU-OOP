from abc import ABC, abstractmethod


class BaseEquipment(ABC):
    def __init__(self, protection: int, price: float):
        self.protection = protection
        self.price = price

    @abstractmethod
    def increase_price(self):
        pass


class ElbowPad(BaseEquipment):
    def __init__(self):
        super().__init__(90, 25)

    def increase_price(self):
        self.price = self.price * 1.1


a = ElbowPad()

print(a.price)
