from typing import List

from project.meals.meal import Meal


class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart: List[Meal] = []
        self.bill: float = 0.0

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value: str):
        is_valid = True
        if len(value) != 10:
            is_valid = False
        elif value[0] != "0":
            is_valid = False
        elif not value.isnumeric():
            is_valid = False

        if is_valid:
            self.__phone_number = value
        else:
            raise ValueError("Invalid phone number!")

