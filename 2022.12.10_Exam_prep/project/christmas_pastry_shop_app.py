from typing import List

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    DELICACY_TYPES = {
        "Gingerbread": Gingerbread,
        "Stolen": Stolen
    }

    BOOTH_TYPES = {
        "Open Booth": OpenBooth,
        "Private Booth": PrivateBooth
    }

    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income: float = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        delicacy: Delicacy = next(filter(lambda delicacy: delicacy.name == name, self.delicacies), None)

        if delicacy in self.delicacies:
            raise Exception(f"{name} already exists!")

        if type_delicacy not in self.DELICACY_TYPES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        self.delicacies.append(self.DELICACY_TYPES[type_delicacy](name, price))
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        booth: Booth = next(filter(lambda booth: booth.booth_number == booth_number, self.booths), None)

        if booth in self.booths:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.BOOTH_TYPES:
            raise Exception(f"{type_booth} is not a valid booth!")

        self.booths.append(self.BOOTH_TYPES[type_booth](booth_number, capacity))
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        booth: Booth = next(filter(
            lambda booth: booth.capacity >= number_of_people and not booth.is_reserved, self.booths), None)

        if not booth:
            raise Exception(f"No available booth for {number_of_people} people!")

        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth: Booth = next(filter(lambda booth: booth.booth_number == booth_number, self.booths), None)
        delicacy: Delicacy = next(filter(lambda delicacy: delicacy.name == delicacy_name, self.delicacies), None)

        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")

        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def booth_invoice(self, booth: Booth):
        delicacies_bill = 0
        for delicacy in booth.delicacy_orders:
            delicacies_bill += delicacy.price

        total_bill = delicacies_bill + booth.price_for_reservation

        self.income += total_bill

        return (f"Booth {booth.booth_number}:\n"
                f"Bill: {total_bill:.2f}lv.")

    def free_booth(self, booth):
        booth.delicacy_orders.clear()
        booth.is_reserved = False
        booth.price_for_reservation = 0

    def leave_booth(self, booth_number: int):
        booth: Booth = next(filter(lambda booth: booth.booth_number == booth_number, self.booths), None)

        invoice = self.booth_invoice(booth)

        self.free_booth(booth)

        return invoice

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
